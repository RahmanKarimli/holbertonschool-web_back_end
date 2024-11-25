/* eslint-disable */
export default function handleResponseFromAPI(promise) {
  const my_promise = new Promise((resolve, reject) => {
    if (promise) {
      resolve({status: 200, body: 'success'});
    }
    else {
      reject(new Error())
    }
  })

  my_promise.finally(console.log("Got a response from the API"));
}
