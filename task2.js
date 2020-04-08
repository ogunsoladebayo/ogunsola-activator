console.clear();
const records = [
    { principal: 2500, time: 1.8 },
    { principal: 1000, time: 5 },
    { principal: 3500, time: 1 },
    { principal: 2000, time: 3 }
];

function interestCalculator(arr) {
    arr.forEach((record) => {
        if (record.principal >= 2500 && record.time > 1 && record.time < 3) {
            record.rate = 3;
        } else if (record.principal >= 2500 && record.time >= 3) {
            record.rate = 4;
        } else if (record.principal < 2500 || record.time <= 1) {
            record.rate = 2;
        } else {
            record.rate = 1;
        }

        record.Interest = findI(record.principal, record.rate, record.time);
    });
    const interestData = arr;
    console.log(interestData);
    return interestData;
}
const findI = (P, R, T) => (P * R * T) / 100;
interestCalculator(records);