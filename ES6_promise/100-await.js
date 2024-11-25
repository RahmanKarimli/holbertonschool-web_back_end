/* eslint-disable */
import {uploadPhoto, createUser} from './utils';

export default async function asyncUploadUser() {
  const photo = await uploadPhoto()
  const user = await createUser()

  try {
    return {
      photo: photo,
      user: user
    }
  } catch (err) {
    return {
      photo: null,
      user: null
    }
  }
}
