import { createClient } from 'redis';
import { exec } from 'child_process';
import { promisify } from 'util';

// startRedisServer();

const client = createClient();

client.on('error', error => {
  console.log(`Redis client not connected to the server: ${error}`)
});

await client.connect()
  .then(() => {
    console.log('Redis client connected to the server');
  })
  .catch((error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

async function startRedisServer() {
  const execP = promisify(exec);
  await execP('redis-6.0.10/src/redis-server')
    .then(() => {})
    .catch((error) => {
      console.log(error.message);
    });
}
