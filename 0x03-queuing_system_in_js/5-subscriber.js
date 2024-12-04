import redis from 'redis';

const client = redis.createClient();

let errPrefix = 'Redis client not connected to the server: ';
client.on('error', error => {
  console.log(`${errPrefix}${error}`);
});
client.on('ready', () => {
  errPrefix = '';
  console.log('Redis client connected to the server');
})

client.subscribe('holberton school channel');
client.on('message', (channel, message) => {
  if (channel === 'holberton school channel') {
    console.log(message);
    if (message === 'KILL_SERVER') {
      client.unsubscribe();
      client.quit();
    }
  }
});
