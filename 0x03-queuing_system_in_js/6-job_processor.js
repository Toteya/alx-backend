import kue from 'kue';
// import push_notification_code from './6-job_creator';

const jobs = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Send notification to ${phoneNumber}, with message: ${message}`);
}

jobs.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message)
  done();
})
