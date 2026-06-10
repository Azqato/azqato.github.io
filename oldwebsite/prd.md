# PRD — azqato.com Old Website Recreation

## Overview

The original azqato.com was a personal website built on **Google Sites**, serving as a central hub for Azqato's content, community, social links, investment resources, music playlists, and gaming accounts. This document captures the full content inventory and product requirements needed to recreate it faithfully in vanilla HTML/CSS/JS.

---

## Site Metadata

| Field | Value |
|---|---|
| Platform | Google Sites |
| Domain | azqato.com |
| Favicon | Small cat avatar (circular, from Google Sites CDN) |
| Site Name | Azqato |
| Logo | Cat icon + "Azqato" wordmark in nav |

---

## Navigation

Persistent sticky nav bar across all pages.

| Item | Route | Notes |
|---|---|---|
| Logo | `/home` | Cat icon + "Azqato" wordmark |
| Home | `/home` | |
| About | `/about` | |
| Links | `/links` | |
| YouTube | `/youtube` | |
| Search icon | — | Far right; opens site search |

Active page displayed in **bold white** text. All other nav links in normal weight.

---

## Footer

Consistent across all pages.

**Links:**
- Privacy Policy → `/privacy-policy`

**Disclaimer text (verbatim):**
1. "Disclaimer - When you purchase a product or service through links provided on Azqato's website, stream, or any other form of content, Azqato may receive a commission as an affiliate marketer."
2. "Azqato is not a licensed financial advisor, accountant or lawyer and nothing he posts in any form on the internet should be taken as advice."
3. "Everything Azqato posts, says or writes is for entertainment purposes only."

---

## Pages

---

### `/home` — Welcome to Azqato.com!

**Heading:** "Welcome to Azqato.com!"

**Hero section:**
- Left: Profile image (cat avatar in front of YouTube play button backdrop)
- Right: "About Azqato" heading + description text + links

**Hero description text:**
> "[Azqato] is a passionate content creator with a deep love for gaming, investing, music production, and streaming. Explore his [links] and join his [Discord] community to stay updated and connect with others."

**Links in hero text:**
- "links" → `/links`
- "Discord" → `https://discord.com/servers/azqato-768563621952880688`

**Button grid — Row 1:**
| Label | URL |
|---|---|
| Discord | `https://discord.com/servers/azqato-768563621952880688` |
| Twitch | `https://twitch.tv/azqato` |
| Patreon | `https://patreon.com/Azqato` |
| Subscribe | `https://twitch.tv/azqato/subscribe` |
| B5TA | `https://b5ta.com` |
| Support | *(support page or external)* |

**Button grid — Row 2:**
| Label | URL |
|---|---|
| YouTube | `https://youtube.com/@Azqato` |
| Azqato | `https://youtube.com/@Azqato` |
| Mixes | `https://youtube.com/@AzqatoMixes` |
| Streams | `https://youtube.com/@AzqatoStreams` |
| Chills | `https://youtube.com/@AzqatoChills` |
| Twitter | *(azqato.com/Twitter redirect)* |

**Button grid — Row 3:**
| Label | URL |
|---|---|
| Music | `/music` |
| Last.fm | `https://last.fm/user/Azqato` |
| Mixcloud | `https://mixcloud.com/Azqato` |
| Reddit | `https://reddit.com/r/Azqato` |
| Accounts | `/accounts` |
| Facebook | `https://facebook.com/azqato` |

**Button grid — Row 4:**
| Label | URL |
|---|---|
| Invests | `/invests` |
| M1 Finance | `https://m1.finance/BVZBG3OqOfMj` |
| Public.com | `https://public.com/user-referral?referrer=Azqato` |
| Instagram | `https://instagram.com/azqato` |
| Tumblr | `https://azqato.tumblr.com` |
| Medium | `https://medium.com/@azqato` |

---

### `/about` — About Azqato

**Heading:** "About Azqato"

**Hero section:**
- Left: Profile image (cat avatar, different pose/background from home)
- Right: Pronunciation + intro paragraph

**Pronunciation subheading (italic):** "Azz - Kah - Toe"

**Bio text (verbatim paragraphs):**

> "From a young age, Azqato, known to many as zoop, developed a love for gaming that has only grown over the years. What began as a passion for playing video games with friends evolved into a drive to build communities that bring people together. Today, he channels that passion into his role as a content creator, web developer, and community leader."

> "Azqato's journey in content creation spans multiple platforms, including Twitch and YouTube, where he shares his adventures in gaming, investing, and music production. His content reflects his belief in living life to the fullest, constantly trying new things, and encouraging others to do the same."

> "One of his most notable achievements is the creation of [B5TA], a thriving community on RuneScape and [Discord]. Through B5TA, Azqato has cultivated a space where gamers of all skill levels can connect, share their experiences, and build lasting friendships. It's a place that embodies his vision of inclusivity and camaraderie in gaming."

> "As an aspiring web developer, Azqato is currently working on a project aimed at establishing a community that fosters the spread of knowledge, resources, and motivation. He is dedicated to empowering others through collaboration and support. For those who generously contribute to his vision, he extends his deepest gratitude."

**Links in body text:**
- "B5TA" → `https://www.b5ta.com/`
- "Discord" → `https://discord.com/servers/azqato-768563621952880688`

---

### `/links` — Azqato's Links

**Heading:** "Azqato's Links"

**All buttons (label → URL):**

| Label | URL |
|---|---|
| Discord | `https://discord.gg/39JrFNY7qS` |
| Patreon | `https://patreon.com/Azqato` |
| Twitch | `https://twitch.tv/azqato` |
| Subscribe | `https://twitch.tv/azqato/subscribe` |
| B5TA | `https://b5ta.com` |
| Last.fm | `https://last.fm/user/Azqato` |
| YouTube | `https://youtube.com/@Azqato` |
| Azqato *(channel)* | `https://youtube.com/@Azqato` |
| Mixes | `https://youtube.com/@AzqatoMixes` |
| Streams | `https://youtube.com/@AzqatoStreams` |
| Chills | `https://youtube.com/@AzqatoChills` |
| Mixcloud | `https://mixcloud.com/Azqato` |
| Instagram | `https://instagram.com/azqato` |
| Music | `/music` |
| Twitter | `https://azqato.com/Twitter` *(redirect)* |
| Reddit | `https://reddit.com/r/Azqato` |
| Accounts | `/accounts` |
| Facebook | `https://facebook.com/azqato` |
| Invests | `/invests` |
| M1 Finance | `https://m1.finance/BVZBG3OqOfMj` |
| Public.com | `https://public.com/user-referral?referrer=Azqato` |
| Discord *(row 4)* | `https://discord.gg/39JrFNY7qS` |
| Tumblr | `https://azqato.tumblr.com` |
| Medium | `https://medium.com/@azqato` |

Layout: 6-column button grid, 4 rows.

---

### `/youtube` — Azqato's Youtube Channels

**Heading:** "Azqato's Youtube Channels"

**Channels (thumbnail image + label + link):**

| Channel Name | URL |
|---|---|
| Azqato | `https://www.youtube.com/@Azqato` |
| Azqato Streams | `https://www.youtube.com/channel/UCar9s_yiJUFWnM-20fLU5dw` |
| Azqato Mixes | `https://www.youtube.com/channel/UCV2X1axZ19iubEzgkouPSCQ` |
| Azqato Chills | `https://www.youtube.com/channel/UC1ytKNtxdBWCiiSQ6DGsxHA` |

Layout: 4 channel cards in a row. Each card has a thumbnail image and the channel name as a link below it. The first channel (Azqato) has a green circular border/ring on its thumbnail.

---

### `/invests` — Azqato Invests

**Heading:** "Azqato Invests"

**Intro text:**
> "Azqato Invests is a community established by Azqato in order to offer a platform for new traders to learn about the financial investment industry."

**Mission:** Equipping new traders with knowledge and fostering networking opportunities for experienced investors.

**Discord CTA text:**
> "A Discord server serves as the primary community platform, a platform where members can interact with each other, share their experiences and exchange valuable information about the financial investment industry."

> "If you would like to add more high-quality resources to this list come join the Discord above and send Azqato a private message."

**All resource links by section:**

**Platforms:**
| Label | URL |
|---|---|
| Robinhood | `http://join.robinhood.com/robertg273` |
| M1 Finance | `https://m1.finance/BVZBG3OqOfMj` |

**Careers:**
| Label | URL |
|---|---|
| Remote Jobs | `https://www.roberthalf.com/jobs/remote` |
| Remotive | `https://remotive.com/` |

**ETFs:**
| Label | URL |
|---|---|
| US Economy | `https://m1.finance/lg6DhArFe7mR` |
| Dividends | `https://m1.finance/aYecv1jT7ATx` |
| Growth | `https://m1.finance/AODxtLWiUWzS` |
| Market Sentiment | `https://m1.finance/wXPV0G6wQG9s` |
| Vanguard | `https://m1.finance/ZONqRA-E4jfh` |
| High Dividend & Low Volatility | `https://m1.finance/Bded182o2HL5` |
| US Government Bonds | `https://m1.finance/qsKTrzlzfl6d` |

**Companies:**
| Label | URL |
|---|---|
| Software | `https://m1.finance/Ql1-1ZBHVG6T` |
| Telecom | `https://m1.finance/InXZI6AHxrEt` |
| Networking | `https://m1.finance/GMRwAaWa07j_` |
| Banks | `https://m1.finance/Do0WxUtoL6A7` |

**Ratings:**
| Label | URL |
|---|---|
| Top Rated Stocks | `https://www.thestreet.com/stock-market-news/10579592/top-rated-stocks/top-rated-stocks.html` |
| Top Rated ETFs | `https://www.thestreet.com/stock-market-news/10575864/top-rated-etfs/top-rated-etfs.html` |

**Screeners:**
| Label | URL |
|---|---|
| TradingView Stock Screener | `https://www.tradingview.com/screener/` |
| Collection of Finviz Screeners (Reddit) | `https://www.reddit.com/r/FluentInFinance/comments/mf7nk0/collection_of_finviz_screeners/` |
| Finviz Screener | `https://finviz.com/screener.ashx` |

**Real Estate:**
| Label | URL |
|---|---|
| Redfin | `https://www.redfin.com/` |
| Areavibes | `https://www.areavibes.com/` |
| Sacramento | `https://www.sacramentocondomania.com` |
| Denver | `https://www.denvercondomania.com` |
| Tempe | `https://www.tempecondomania.com/` |
| Las Vegas | `https://www.lasvegascondomania.com/` |
| San Diego | `https://www.sandiegocondomania.com/` |
| Orange County | `https://www.orangecountycondomania.com/` |
| San Jose | `https://www.sanjosecondomania.com/` |

**Charts:**
| Label | URL |
|---|---|
| Stock Charts — Free Charts | `https://stockcharts.com/freecharts/` |
| RobinTrack | `https://robintrack.net/` |

**Databases:**
| Label | URL |
|---|---|
| ETFDB.com | `https://etfdb.com/etfs/` |
| Dividend.com | `https://www.dividend.com/` |
| Dividend Stocks Online | `https://dividendstocksonline.com/` |

**Economic Indicators:**
| Label | URL |
|---|---|
| Truflation | `https://truflation.com/` |
| Investopedia Economic Indicator | `https://www.investopedia.com/terms/e/economic_indicator.asp` |
| YCharts Sentiment | `https://ycharts.com/indicators/us_investor_sentiment_bull_bear_spread` |
| Census Economic Indicators | `https://www.census.gov/economic-indicators/` |
| Trading Economics | `https://tradingeconomics.com/indicators` |

**Education:**
| Label | URL |
|---|---|
| Investopedia | `https://www.investopedia.com/` |
| Coursera Investment Strategy | `https://www.coursera.org/specializations/investment-strategy` |
| Investopedia ETF Guide | `https://www.investopedia.com/terms/e/etf.asp` |
| Investopedia Averaging Down | `https://www.investopedia.com/terms/a/averagedown.asp` |
| Investopedia EPS | `https://www.investopedia.com/terms/e/eps.asp` |
| Zacks Trading Earnings Calendar | `https://finance.zacks.com/make-money-trading-earnings-calendar-11148.html` |
| Study.com Leveraged ETF Decay | `https://study.com/academy/lesson/what-is-a-leveraged-etf-decay-risk-volatility.html` |
| Investopedia Inverse ETF | `https://www.investopedia.com/terms/i/inverse-etf.asp` |
| Investopedia Stop Loss Orders | `https://www.investopedia.com/ask/answers/06/stoplossorderdetails.asp` |
| Investopedia Support and Resistance | `https://www.investopedia.com/trading/support-and-resistance-basics/` |
| Investopedia Moving Average | `https://www.investopedia.com/terms/m/movingaverage.asp` |
| Investopedia MACD | `https://www.investopedia.com/terms/m/macd.asp` |
| Investopedia Beta | `https://www.investopedia.com/terms/b/beta.asp` |
| Investopedia Volatility | `https://www.investopedia.com/terms/v/volatility.asp` |

**Guides:**
| Label | URL |
|---|---|
| Stock Ratios Guide | `https://docs.google.com/document/d/1pjHqe-QKjiutLtAnELCEonIEIJ4IrcVSE_ZJKbuBcMY/edit?usp=sharing` |
| Options Basics Tutorial | `https://www.investopedia.com/options-basics-tutorial-4583012` |
| Asset Allocation Guide | `https://www.lynalden.com/asset-allocation/` |

**Indices:**
| Label | URL |
|---|---|
| TradingView Major Indices | `https://www.tradingview.com/markets/indices/quotes-major/` |

**Information:**
| Label | URL |
|---|---|
| Google Finance | `https://google.com/finance` |
| Yahoo Finance | `https://finance.yahoo.com/` |
| WolframAlpha | `https://wolframalpha.com/` |
| Investopedia | `https://www.investopedia.com/` |
| TradingView | `https://www.tradingview.com/` |
| Finviz | `https://finviz.com/` |
| Seeking Alpha | `https://seekingalpha.com/` |

**News:**
| Label | URL |
|---|---|
| Renaissance Capital IPO Calendar | `https://renaissancecapital.com/IPO-Center/Calendar` |
| NewsNow Oil Prices | `https://www.newsnow.co.uk/h/Business+&+Finance/Oil+Prices` |
| Seeking Alpha Market News | `https://seekingalpha.com/market-news/top-news` |
| YouTube Channel (Finance) | `https://www.youtube.com/channel/UCIALMKvObZNtJ6AmdCLP7Lg` |
| YouTube Channel (Finance 2) | `https://www.youtube.com/channel/UCrp_UI8XtuYfpiqluWLD7Lw` |
| Daily FX News | `https://www.youtube.com/user/DailyFXNews` |

---

### `/music` — Music

**Heading:** "Music"

**Intro text:** "Check out my Spotify playlists!"

**Spotify Profile:** `https://open.spotify.com/user/ju4cn8wu8geoowmu3tdxkfh1e`

**Playlists:**

| Name | Subtitle | URL |
|---|---|---|
| BANGERS | Feat. Drops | `https://open.spotify.com/playlist/1G4IJbM8jnz23AngZKeiC0?si=64874833d97f42d6` |
| ADDICTIONS | Feat. Vocals | `https://open.spotify.com/playlist/7KePad2TWMrmXvEdZqmIPA?si=5ba79216d83f445d` |

---

### `/accounts` — Accounts

**Heading:** *(implied "Accounts")*

**Gaming accounts by platform:**

**Steam:**
- Azqato *(link not captured)*

**League of Legends:**
- Chief Rocka → op.gg profile
- Azqato → op.gg profile

**Teamfight Tactics:**
- Chief Rocka → lolchess.gg profile
- Azqato → lolchess.gg profile

**Runescape:**
- zoop → runeclan.com profile
- Hctibaru → runeclan.com profile

---

## Out of Scope (Not Recreating)

- Google Sites platform infrastructure
- Google Sites search functionality
- "Report abuse" footer element
- Google Sites CDN image URLs (original images will need to be re-hosted or approximated)
