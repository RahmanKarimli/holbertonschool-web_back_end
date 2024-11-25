/* eslint-disable */
import {uploadPhoto, createUser} from './utils';

export default function handleProfileSignup() {
  const promises = new Promise.all([uploadPhoto(), createUser()]);

  return promises
    .then(message => {
      const photo = message[0]
      const user = message[1]

      console.log(`${photo.body} ${user.firstName} ${user.lastName}`)
    })
    .catch(() => console.log("Signup system offline"));
}
