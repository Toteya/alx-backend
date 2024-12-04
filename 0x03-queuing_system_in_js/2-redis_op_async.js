import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', error => {
  console.log(`Redis client not connected to the server: ${error}`)
});
client.on('ready', () => {
  console.log('Redis client connected to the server');
})

const setP = promisify(client.set).bind(client);
const getP = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
  await setP(schoolName, value)
    .then(() => {
      console.log('Reply: OK');
    });
}

async function displaySchoolValue(schoolName) {
  const value = await getP(schoolName);
  console.log(value);
}

await displaySchoolValue('Holberton');
await setNewSchool('HolbertonSanFrancisco', '100');
await displaySchoolValue('HolbertonSanFrancisco');
