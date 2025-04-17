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

      return {
        status,
        message: responseData?.message || axiosError.message || "Unknown error",
        details: responseData?.details || responseData,
      };
    }

    // For non-Axios errors
    return {
      status: 500,
      message: error instanceof Error ? error.message : "Unknown error",
    };
  }
}
