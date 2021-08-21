const globalMaxYear = new Date().getFullYear();

export function parseYear(dateString) {
    // get a year from DD-MM-YYYY
    return parseInt(dateString.split('-').pop())
}

export function validYear(year) {
    if (year <= globalMaxYear && year >= 1966) {
        return true
    }
    return false
}