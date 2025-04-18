// Test script for the Lightfeed TypeScript client
const { LightfeedClient } = require("lightfeed");

// Initialize client with your API key
const client = new LightfeedClient({
  apiKey: "test-api-key",
});

async function testClient() {
  try {
    console.log("Testing Lightfeed TypeScript client...");
    console.log("Client instance created successfully");
    console.log("Client configuration:");
    console.log(`- API key: ${client.config.apiKey}`);
    console.log(`- Base URL: ${client.config.baseUrl}`);
    console.log(`- Timeout: ${client.config.timeout}`);

    // Mock API calls for testing
    // In a real scenario, you would use actual API keys and databases
    console.log("\nTest successful! The client is correctly installed.");
  } catch (error) {
    console.error("Test failed with error:", error);
  }
}

testClient();
