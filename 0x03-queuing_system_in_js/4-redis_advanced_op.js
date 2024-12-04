import redis from 'redis';

let errPrefix = 'Redis client not connected to the server: ';

const client = redis.createClient();
client.on('error', error => {
  console.log(`${errPrefix}${error}`);
});
client.on('ready', () => {
  errPrefix = '';
  console.log('Redis client connected to the server');
})

client.hset('HolbertonSchools', 'Portland', 50, redis.print);
client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
client.hset('HolbertonSchools', 'New York', 20, redis.print);
client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
client.hset('HolbertonSchools', 'Cali', 40, redis.print);
client.hset('HolbertonSchools', 'Paris', 2, redis.print);

client.hgetall('HolbertonSchools', (err, obj) => {
  if (err) {
    console.log(err)
  } else console.log(obj);
})
