import kue from 'kue';
import redis from 'redis';

// const jobs = kue.createQueue();
const jobData = {
  phoneNumber: '',
  message: '',
}

const push_notification_code = kue.createQueue();
const job = push_notification_code.createJob(jobData)
  .save((err) => {
    if (err ) console.log(`Notification job failed: ${err}`);
    else {
      console.log(`Notification job created: ${job.id}`);
      console.log(`Notification job completed`)
    }
  });
