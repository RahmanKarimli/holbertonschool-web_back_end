/* eslint-disable */
export default function handleResponseFromAPI(promise) {
  const my_promise = new Promise((resolve, reject) => {
    if (promise) {
      resolve({status: 200, body: 'Success'});
    }
    else {
      reject(new Element())
    }
  })

  my_promise.finally(console.log("Got a response from the API"));
}
