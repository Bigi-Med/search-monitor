import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 1,  // Virtual Users
  duration: '24h',  // Duration of the test
};

export default function () {
  // Replace 'http://example.com' with the actual server URL you want to request.
  let response = http.get('http://192.168.1.20:5000');

  if (response.status === 200) {
    console.log('Request sent successfully');
  } else {
    console.log(`Failed to send request. Status code: ${response.status}`);
  }

  // Sleep for 24 hours
  sleep(2*60*60);  // Sleep for 24 hours in seconds
}
