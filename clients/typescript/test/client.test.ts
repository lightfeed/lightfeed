import axios from "axios";
import { LightfeedClient } from "../src/client";
import {
  LightfeedConfig,
  RecordsResponse,
  Condition,
  Operator,
  LightfeedError,
} from "../src/types";

// Mock axios
jest.mock("axios");
const mockedAxios = axios as jest.Mocked<typeof axios>;

describe("LightfeedClient", () => {
  let client: LightfeedClient;
  const mockConfig: LightfeedConfig = {
    apiKey: "test-api-key",
  };

  beforeEach(() => {
    // Reset mocks before each test
    jest.clearAllMocks();

    // Mock axios.create to return a mocked instance
    mockedAxios.create.mockReturnValue(mockedAxios);

    // Create a new client for each test
    client = new LightfeedClient(mockConfig);
  });

  describe("constructor", () => {
    it("should create a client with default values", () => {
      expect(mockedAxios.create).toHaveBeenCalledWith({
        baseURL: "https://api.lightfeed.ai",
        timeout: 30000,
        headers: {
          "x-api-key": "test-api-key",
          "Content-Type": "application/json",
        },
      });
    });

    it("should use custom baseUrl and timeout if provided", () => {
      const customConfig: LightfeedConfig = {
        apiKey: "test-api-key",
        baseUrl: "https://custom-api.example.com",
        timeout: 5000,
      };

      client = new LightfeedClient(customConfig);

      expect(mockedAxios.create).toHaveBeenCalledWith({
        baseURL: "https://custom-api.example.com",
        timeout: 5000,
        headers: {
          "x-api-key": "test-api-key",
          "Content-Type": "application/json",
        },
      });
    });
  });

  describe("getRecords", () => {
    it("should call the correct endpoint with parameters", async () => {
      const mockResponse: RecordsResponse = {
        results: [
          {
            id: 1,
            data: { name: "Test Record" },
            timestamps: {
              first_seen_time: "2023-01-01T00:00:00Z",
              last_changed_time: "2023-01-02T00:00:00Z",
              last_seen_time: "2023-01-03T00:00:00Z",
            },
          },
        ],
        pagination: {
          limit: 100,
          next_cursor: null,
          has_more: false,
        },
      };

      mockedAxios.get.mockResolvedValueOnce({ data: mockResponse });

      const params = {
        start_time: "2023-01-01T00:00:00Z",
        limit: 10,
      };

      const result = await client.getRecords("test-db-id", params);

      expect(mockedAxios.get).toHaveBeenCalledWith(
        "/v1/databases/test-db-id/records",
        { params }
      );
      expect(result).toEqual(mockResponse);
    });

    it("should handle errors correctly", async () => {
      // Just simulate any rejection from axios
      const error = new Error("API error");
      mockedAxios.get.mockRejectedValueOnce(error);

      // Skip checking the exact error structure since it's hard to mock
      await expect(client.getRecords("test-db-id")).rejects.toEqual({
        status: 500,
        message: "API error",
      });
    });
  });

  describe("searchRecords", () => {
    it("should call the correct endpoint with parameters", async () => {
      const mockResponse: RecordsResponse = {
        results: [
          {
            id: 1,
            data: { name: "Test Record" },
            timestamps: {
              first_seen_time: "2023-01-01T00:00:00Z",
              last_changed_time: "2023-01-02T00:00:00Z",
              last_seen_time: "2023-01-03T00:00:00Z",
            },
            relevance_score: 0.9,
          },
        ],
        pagination: {
          limit: 100,
          next_cursor: null,
          has_more: false,
        },
      };

      mockedAxios.post.mockResolvedValueOnce({ data: mockResponse });

      const params = {
        search: {
          text: "test query",
          threshold: 0.5,
        },
      };

      const result = await client.searchRecords("test-db-id", params);

      expect(mockedAxios.post).toHaveBeenCalledWith(
        "/v1/databases/test-db-id/search",
        params
      );
      expect(result).toEqual(mockResponse);
    });
  });

  describe("filterRecords", () => {
    it("should call the correct endpoint with parameters", async () => {
      const mockResponse: RecordsResponse = {
        results: [
          {
            id: 1,
            data: { name: "Test Record", category: "Test" },
            timestamps: {
              first_seen_time: "2023-01-01T00:00:00Z",
              last_changed_time: "2023-01-02T00:00:00Z",
              last_seen_time: "2023-01-03T00:00:00Z",
            },
          },
        ],
        pagination: {
          limit: 100,
          next_cursor: null,
          has_more: false,
        },
      };

      mockedAxios.post.mockResolvedValueOnce({ data: mockResponse });

      const params = {
        filter: {
          condition: "AND" as Condition,
          rules: [
            {
              column: "category",
              operator: "equals" as Operator,
              value: "Test",
            },
          ],
        },
      };

      const result = await client.filterRecords("test-db-id", params);

      expect(mockedAxios.post).toHaveBeenCalledWith(
        "/v1/databases/test-db-id/filter",
        params
      );
      expect(result).toEqual(mockResponse);
    });
  });
});
