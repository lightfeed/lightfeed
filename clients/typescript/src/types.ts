/**
 * Lightfeed API Client type definitions
 */

/**
 * API client configuration
 */
export interface LightfeedConfig {
  /** Lightfeed API key */
  apiKey: string;
  /** API base URL (defaults to https://api.lightfeed.ai) */
  baseUrl?: string;
  /** Request timeout in milliseconds (defaults to 30000) */
  timeout?: number;
}

/**
 * Timestamp object for records
 */
export interface Timestamps {
  /** ISO 8601 timestamp when the record was first seen */
  created_at: string;
  /** ISO 8601 timestamp when the record was last changed */
  changed_at: string;
  /** ISO 8601 timestamp when the record was last seen */
  synced_at: string;
}

/**
 * Record returned by the API
 */
export interface LightfeedRecord {
  /** Unique identifier for the record */
  id: number;
  /** The record's structured data */
  data: Record<string, any>;
  /** Timing information for the record */
  timestamps: Timestamps;
  /** Relevance score (only present if semantic search is applied) */
  relevance_score?: number;
}

/**
 * Pagination metadata
 */
export interface Pagination {
  /** The requested limit parameter value from the original request */
  limit: number;
  /** Token to use for fetching the next page */
  next_cursor: string | null;
  /** Indicates whether more results are available */
  has_more: boolean;
}

/**
 * API response with records and pagination
 */
export interface RecordsResponse {
  /** List of records */
  results: LightfeedRecord[];
  /** Pagination information */
  pagination: Pagination;
}

/**
 * Query parameters for retrieving records
 */
export interface GetRecordsParams {
  /** Start of last seen time range (ISO 8601 timestamp) */
  start_time?: string;
  /** End of last seen time range (ISO 8601 timestamp) */
  end_time?: string;
  /** Maximum number of records to return (default: 100, max: 500) */
  limit?: number;
  /** Cursor for pagination (from previous response) */
  cursor?: string;
}

/**
 * Time range for filtering records
 */
export interface TimeRange {
  /** Start of last seen time range (ISO 8601 timestamp) */
  start_time?: string;
  /** End of last seen time range (ISO 8601 timestamp) */
  end_time?: string;
}

/**
 * Pagination parameters for search/filter
 */
export interface PaginationParams {
  /** Maximum number of records to return (default: 100, max: 500) */
  limit?: number;
  /** Cursor for pagination (from previous response) */
  cursor?: string;
}

/**
 * Semantic search parameters
 */
export interface SearchParams {
  /** The text to search for */
  text: string;
  /** Minimum relevance score threshold (0 to 1, defaults to 0.2) */
  threshold?: number;
}

/**
 * Condition type for filter rules
 */
export type Condition = "AND" | "OR";

/**
 * Comparison operators for filter rules
 */
export type Operator =
  | "equals"
  | "not_equals"
  | "greater_than"
  | "less_than"
  | "greater_than_or_equals"
  | "less_than_or_equals"
  | "contains"
  | "not_contains"
  | "starts_with"
  | "ends_with"
  | "is_empty"
  | "is_not_empty";

/**
 * Simple filter rule for a single column
 */
export interface ColumnRule {
  /** The column name to filter on */
  column: string;
  /** The comparison operator */
  operator: Operator;
  /** The value to compare with */
  value?: any;
}

/**
 * Group of filter rules with a logical condition
 */
export interface RuleGroup {
  /** Logical operator to combine rules (AND/OR) */
  condition: Condition;
  /** List of rules or rule groups */
  rules: (ColumnRule | RuleGroup)[];
}

/**
 * Filter definition for search or filter API
 */
export type Filter = RuleGroup;

/**
 * Parameters for search records API
 */
export interface SearchRecordsParams {
  /** Semantic search parameters */
  search: SearchParams;
  /** Filter to apply (optional) */
  filter?: Filter;
  /** Time range to filter by (optional) */
  time_range?: TimeRange;
  /** Pagination parameters (optional) */
  pagination?: PaginationParams;
}

/**
 * Parameters for filter records API
 */
export interface FilterRecordsParams {
  /** Filter to apply */
  filter: Filter;
  /** Time range to filter by (optional) */
  time_range?: TimeRange;
  /** Pagination parameters (optional) */
  pagination?: PaginationParams;
}

/**
 * API error status codes
 */
export type LightfeedErrorStatus =
  | 400 // Bad Request: Invalid request parameters
  | 401 // Unauthorized: Invalid or missing API key
  | 403 // Forbidden: The API key doesn't have permission
  | 404 // Not Found: The requested resource doesn't exist
  | 429 // Too Many Requests: Rate limit exceeded
  | 500; // Internal Server Error: Something went wrong on our end

/**
 * Error from the Lightfeed API
 */
export interface LightfeedError {
  /** HTTP status code */
  status: LightfeedErrorStatus;
  /** Error message */
  message: string;
}
