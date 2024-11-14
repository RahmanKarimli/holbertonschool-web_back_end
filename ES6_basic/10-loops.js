/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
    const new_array = array;
    for (const value of array) {
        const index = array.indexOf(value);
        new_array[index] = appendString + value;
    }

  return new_array;
}