/**
 * Lightfeed API Client Library
 *
 * This library provides a convenient way to interact with the Lightfeed API to access
 * your extracted web data programmatically.
 */

export { LightfeedClient } from "./client";
export * from "./types";

// Export default as the client for convenience
import { LightfeedClient } from "./client";
export default LightfeedClient;
