/* eslint-disable */
export default function hasValuesFromArray(set, arr) {
  let exists = false;

  for (let i = 0; i < arr.length; i++) {
    exists = set.has(arr[i]);
  }
  return exists;
}
