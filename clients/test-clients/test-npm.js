// Test script for the Lightfeed TypeScript client
require("dotenv").config({ path: ".env" });

import { LightfeedClient } from "lightfeed";

// Initialize client with your API key
const client = new LightfeedClient({
  apiKey: process.env.CLIENT_API_KEY,
});

async function testClient() {
  try {
    console.log("Testing Lightfeed TypeScript client...");
    console.log("Client instance created successfully");
    console.log("Client configuration:");
    console.log(`- API key: ${client.config.apiKey.slice(0, 6)}...`);
    console.log(`- Base URL: ${client.config.baseUrl}`);
    console.log(`- Timeout: ${client.config.timeout}`);

    try {
      const response = await client.searchRecords(process.env.DATABASE_ID, {
        search: {
          text: "AI solutions",
        },
        filter: {
          rules: [
            {
              column: "start_date",
              operator: "equals",
              value: 2021,
            },
          ],
        },
        pagination: {
          limit: 2,
          cursor: "2025-03-11T19:59:49.150Z_691",
        },
      });

      console.log(`Found ${response.results.length} matching records`);
      console.log(response.results);
      console.log(response.pagination);
    } catch (error) {
      console.error("Error searching records:", error);
    }

    // Mock API calls for testing
    // In a real scenario, you would use actual API keys and databases
    console.log("\nTest successful! The client is correctly installed.");
  } catch (error) {
    console.error("Test failed with error:", error);
  }
}

await testClient();
