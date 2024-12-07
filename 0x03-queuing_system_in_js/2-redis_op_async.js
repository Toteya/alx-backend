import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('error', error => {
  console.log(`Redis client not connected to the server: ${error}`)
});
client.on('ready', () => {
  console.log('Redis client connected to the server');
})

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value)
    .then((reply) => {
      console.log(`Reply: ${reply}`);
    })
    .catch((err) => {});
}

async function displaySchoolValue(schoolName) {
  await getAsync(schoolName)
    .then((reply) => {
      console.log(reply);
    })
    .catch((err) => {});
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
