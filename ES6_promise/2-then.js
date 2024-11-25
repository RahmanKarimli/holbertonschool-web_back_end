/* eslint-disable */
export default function handleResponseFromAPI(promise) {
  const my_promise = new Promise((resolve, reject) => {
    if (promise) {
      resolve({body: 'success', status: 200});
    }
    else {
      reject(new Error())
    }
  })

  my_promise.finally(console.log("Got a response from the API"));
}
