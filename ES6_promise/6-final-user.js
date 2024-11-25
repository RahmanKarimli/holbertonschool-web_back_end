/* eslint-disable */
import signUpUser from './4-user-promise.js'
import uploadPhoto from './5-photo-reject.js'

export default function handleProfileSignup(first, last, file) {
  const promises = [signUpUser(first, last), uploadPhoto(file)]

  return Promise.allSettled(promises)
    .then((results) => results.map((result) => {
      if (result.status === 'rejected') {
        return {
          status: 'rejected',
          value: `Error: ${result.reason.message}`
        }
      }
      return result
    }));
}
