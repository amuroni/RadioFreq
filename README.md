# RadioFreq

This project aims to collect all national radio frequencies (Italy in my case) via HTML scraping.

So far I managed to get all the frequencies divided by region (and municipality for each region) with the requests library.
I collected the table content of each url, scraped from each html, format it with beautifulsoup and created an excel file as a container for future use (like a database)

I started with GetFreq.py, which collects all the needed frequencies data from a website.

The first issue I ran into was that I wanted to collect all the data (for each url) at the same time, not one url at a time (that would be unnecessary boring, inefficient and requires too much repetitive code anyway)

To do that, I created a list of urls, and thn started a for loop to cycle through urls

From the urls list, the for loop operates as follows:
  - do a requests.get on the url
  - call bsoup and get the raw html content
  - look for the table content with soup.findAll in each url HTML content.
  - read the html with pandas to get it in a decent, readable format
  - you now have a dataframe, sorta

At this stage of the for loop, if you print(dfs) you get the for loop to print each table and the data it holds (which I did as a doublecheck to be sure I was going the right way).

Now, to transfer all of this on excel: the issue here is that pd.read_html returns a list item, not a dataframe.
And list don't work with pandas, since it only accepts dataframes.

However, I noted that the dataframe df for each dfs = dfs[0].
So I declared df = dfs[0] and the for loop continued to convert each list into a dataframe, which is usable with the pandas library.

Next up, with df.to_excel, I wanted to push the dataframe into an excel doc named "Frequencytable.xlsx" (see it declared in writer, before the loop starts)
It's all fine and easy, until each dataframe overwrites the previous one and you're left with a mess of an excel.

Quick fix: let each dataframe start below the previous one.
I used len(df.index), which basically returns the number of rows of each dataframe.

In df.to_excel I assigned startrow = row, and let row be row + n. of wors of preceding df +1.
This way, the dataframes will not be overwriting each other, thus deleting information in the process.

Then by adding writer.save() I closed the for loop properly and saved all data.

Done, now the xlsx file is 11k rows long and contains all the data I need!

Next up, I'll add a way to scan for specific data in the xlsx file, and maybe allow a user to do it via input commands.

