import kue from 'kue';
import redis from 'redis';

// const jobs = kue.createQueue();
const jobData = {
  phoneNumber: '',
  message: '',
}

const push_notification_code = kue.createQueue();
const job = push_notification_code.create('push_notification_code', jobData)
  .save((err) => {
    if (err ) console.log(err);
    else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', () => {
  console.log(`Notification job completed`);
})
job.on('failed', () => {
  console.log(`Notification job failed`);
})