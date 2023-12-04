const puppeteer = require('puppeteer');

(async () => {
  // To launch browser
  const browser = await puppeteer.launch();

  // To create a new page
  const page = await browser.newPage();

  // To navigate to the website
  await page.goto('https://abrahamjuliot.github.io/creepjs/'); // Replace with the actual URL

  // Wait for the elements to be present
  await page.waitForSelector('div span.unblurred');
  await page.waitForSelector('div div');
  await page.waitForSelector('div.unblurred');
  await page.waitForSelector('.ellipsis-all');

  // To extract information
  const trustScore = await page.$eval('div span.unblurred', (element) => element.textContent.trim());
  const lies = await page.$eval('div div', (element) => element.textContent.trim());
  const botInfo = await page.$eval('div.unblurred', (element) => element.textContent.trim());
  const fingerprint = await page.$eval('.ellipsis-all', (element) => element.textContent.trim());

  // To create JSON object
  const data = {
    trustScore,
    lies,
    botInfo,
    fingerprint,
  };

  // Save JSON
  const fs = require('fs');
  fs.writeFileSync('data.json', JSON.stringify(data, null, 2));

  // To create PDF of the page
  await page.pdf({ path: 'Resultt.pdf', format: 'A4' });

  // Log the extracted information
  // console.log('Trust Score:', trustScore);
  // console.log('Lies:', lies);
  // console.log('Bot Information:', botInfo);
  // console.log('Fingerprint:', fingerprint);

  // Close the browser
  await browser.close();
})();
