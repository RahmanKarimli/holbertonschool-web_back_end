/* eslint-disable */
export default function cleanSet(set, startString) {
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  return [...set]
    .filter(value => value.startsWith(startString))
    .map(filtered => filtered.slice(startString.length, filtered.length))
    .join('-');
}
