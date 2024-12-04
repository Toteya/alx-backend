import redis from 'redis';
import { exec } from 'child_process';
import { promisify } from 'util';

// startRedisServer();

const client = redis.createClient();

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
    .then(() => console.log('Redis-server started'))
    .catch((error) => console.log(error));
}

async function setNewSchool(schoolName, value) {
  const reply = await client.set(schoolName, value);
  console.log(`Reply: ${reply}`);
}

async function displaySchoolValue(schoolName) {
  console.log(await client.get(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
