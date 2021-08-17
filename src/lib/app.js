import { readable } from 'svelte/store'
import data from '../../static/archive.json'

export const archive = readable(data.archive);