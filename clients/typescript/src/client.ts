/**
 * Lightfeed API Client
 */
import axios, { AxiosInstance, AxiosError } from "axios";
import {
  LightfeedConfig,
  RecordsResponse,
  GetRecordsParams,
  SearchRecordsParams,
  FilterRecordsParams,
  LightfeedError,
  LightfeedErrorStatus,
} from "./types";

/**
 * Default configuration values
 */
const DEFAULT_BASE_URL = "https://api.lightfeed.ai";
const DEFAULT_TIMEOUT = 30000; // 30 seconds

/**
 * Lightfeed API Client
 *
 * Client for interacting with the Lightfeed API to access your extracted web data.
 */
export class LightfeedClient {
  private readonly httpClient: AxiosInstance;
  private readonly config: Required<LightfeedConfig>;

  /**
   * Creates a new Lightfeed API client
   *
   * @param config Client configuration
   */
  constructor(config: LightfeedConfig) {
    this.config = {
      apiKey: config.apiKey,
      baseUrl: config.baseUrl || DEFAULT_BASE_URL,
      timeout: config.timeout || DEFAULT_TIMEOUT,
    };

    this.httpClient = axios.create({
      baseURL: this.config.baseUrl,
      timeout: this.config.timeout,
      headers: {
        "x-api-key": this.config.apiKey,
        "Content-Type": "application/json",
      },
    });
  }

  /**
   * Get all records from a database with optional filters
   *
   * @param databaseId The database ID
   * @param params Optional query parameters
   * @returns Records response containing results and pagination information
   */
  async getRecords(
    databaseId: string,
    params?: GetRecordsParams
  ): Promise<RecordsResponse> {
    try {
      const response = await this.httpClient.get(
        `/v1/databases/${databaseId}/records`,
        {
          params,
        }
      );
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Search records using semantic search with optional filters
   *
   * @param databaseId The database ID
   * @param params Search parameters including search text, filters, and pagination
   * @returns Records response containing results and pagination information
   */
  async searchRecords(
    databaseId: string,
    params: SearchRecordsParams
  ): Promise<RecordsResponse> {
    try {
      const response = await this.httpClient.post(
        `/v1/databases/${databaseId}/search`,
        params
      );
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Filter records using complex filter expressions
   *
   * @param databaseId The database ID
   * @param params Filter parameters including filter rules, time range, and pagination
   * @returns Records response containing results and pagination information
   */
  async filterRecords(
    databaseId: string,
    params: FilterRecordsParams
  ): Promise<RecordsResponse> {
    try {
      const response = await this.httpClient.post(
        `/v1/databases/${databaseId}/filter`,
        params
      );
      return response.data;
    } catch (error) {
      throw this.handleError(error);
    }
  }

  /**
   * Handles and transforms API errors into a consistent format
   *
   * @param error The error from axios
   * @returns A formatted LightfeedError
   */
  private handleError(error: unknown): LightfeedError {
    if (axios.isAxiosError(error)) {
      const axiosError = error as AxiosError;
      const status = axiosError.response?.status || 500;
      const responseData = axiosError.response?.data as any;

      // Validate that status is one of the expected error codes
      // If not, default to 500
      const validStatus = [400, 401, 403, 404, 429, 500].includes(status)
        ? (status as LightfeedErrorStatus)
        : 500;

      return {
        status: validStatus,
        message:
          responseData?.message || this.getDefaultErrorMessage(validStatus),
      };
    }

    // For non-Axios errors
    return {
      status: 500,
      message: error instanceof Error ? error.message : "Unknown error",
    };
  }

  /**
   * Gets a default error message for a given status code
   *
   * @param status HTTP status code
   * @returns A default error message
   */
  private getDefaultErrorMessage(status: LightfeedErrorStatus): string {
    switch (status) {
      case 400:
        return "Invalid request parameters";
      case 401:
        return "Invalid or missing API key";
      case 403:
        return "The API key doesn't have permission to access the resource";
      case 404:
        return "The requested resource doesn't exist";
      case 429:
        return "Rate limit exceeded";
      case 500:
      default:
        return "Something went wrong on our end";
    }
  }
}
