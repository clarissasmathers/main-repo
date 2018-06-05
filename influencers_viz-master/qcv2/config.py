### Configuration

### XTABS CONFIG:

xtab_var_options = {
    "Count" : "COUNT(*) AS count",
    "Percentage": "COUNT(*)::FLOAT / SUM(COUNT(*)) OVER() AS pct",
    "Avg Contribution": "AVG(CASE WHEN contribution_amnt > 0 THEN contribution_amnt ELSE NULL END) AS avg_contribution",
    #"Avg Salary": "AVG(CASE WHEN salary > 0 THEN salary ELSE NULL END) AS avg_salary",
    "Avg Influence": "AVG(influence) AS avg_influence_score",
    "Avg National Influence Rank": "AVG(national_influence_rank) AS avg_natl_influence_rank",
    "Avg State Influence Rank": "AVG(state_influence_rank) AS avg_state_influence_rank",
    "Avg Mail Contactability": "AVG(mail_contact) AS avg_mail_contactability",
    "Avg Digital Contactability": "AVG(digital_contact) AS avg_digital_contactability",
    "Avg Mobile Contactability": "AVG(mobile_contact) AS avg_mobile_contactability",
    "Avg TV Contactability": "AVG(tv_any) AS avg_tv_contactability",
    "Avg Partisan Score": "AVG(c_bl_partisan_score) AS avg_partisan_score",
    "Pct Government": "CAST(CONVERT(DECIMAL(10,2), AVG(all_government*100)) as nvarchar) AS pct_govt",
    "Pct Business": "CAST(CONVERT(DECIMAL(10,2), AVG(all_business*100)) as nvarchar) AS pct_business",
    "Pct Healthcare": "CAST(CONVERT(DECIMAL(10,2), AVG(healthcare*100)) as nvarchar) AS pct_healthcare",
    "Pct Female": "CAST(CONVERT(DECIMAL(10,2), AVG(CASE WHEN CASE WHEN gender = 'Unknown' THEN NULL ELSE gender END = 'Female' THEN 100 ELSE 0 END)) as nvarchar) AS pct_female",
    "PCT 18 to 29": "CAST(CONVERT(DECIMAL(10,2), AVG(CASE WHEN demo_age_bucket_full = 'a18to29' THEN 100 ELSE 0 END)) AS nvarchar) AS pct18to29",
    "PCT 30 to 39": "CAST(CONVERT(DECIMAL(10,2), AVG(CASE WHEN demo_age_bucket_full = 'b30to39' THEN 100 ELSE 0 END)) AS nvarchar) AS pct30to39",
    "PCT 40 to 49": "CAST(CONVERT(DECIMAL(10,2), AVG(CASE WHEN demo_age_bucket_full = 'c40to49' THEN 100 ELSE 0 END)) AS nvarchar) AS pct40to49",
    "PCT 50 to 64": "CAST(CONVERT(DECIMAL(10,2), AVG(CASE WHEN demo_age_bucket_full = 'd50to64' THEN 100 ELSE 0 END)) AS nvarchar) AS pct50to64",
    "PCT 65 plus": "CAST(CONVERT(DECIMAL(10,2), AVG(CASE WHEN demo_age_bucket_full = 'e65plus' THEN 100 ELSE 0 END)) AS nvarchar) AS pct65plus",
    "PCT Federal Level": "CAST(CONVERT(DECIMAL(10,2), AVG(federal_level*100)) AS nvarchar) AS pct_federal",
    "PCT State Level": "CAST(CONVERT(DECIMAL(10,2), AVG(state_level*100)) AS nvarchar) AS pct_state",
    "PCT Local Level": "CAST(CONVERT(DECIMAL(10,2), AVG(local_level*100)) AS nvarchar) AS pct_local"
}

xtab_group_options = ['state', 'influence', 'media_market', 'gender', 'spouse', 'demo_age_bucket_full',
     'density_bucket_full', 'marital_status_bucket',
     'marital_status_x_gender', 'religion_bucket', 'demo_combined_ethnicity_4way',
     'education_modeling', 'donrever_1', 'children', 'retired', 'veteran_1', 'renter',
     'homeowner', 'investor_1', 'demo_income_bucket_full', 'vb_business_owner_indicator',
     'length_of_residence', 'national_influence_decile', 'state_influence_decile',
     'ballotpedia_list','who_leads_officials_list','fec_candidates_list', 'fec_committees_list',
     'fec_contributions_list', 'fec_expenditures_list', 'fec_transactions_list',
     'federal_house_lobbyists_list', 'federal_senate_lobbyists_list', 'forbes_400_list',
     'fortune_500_board_list', 'health_experts_list', 'health_providers_list', 'hospital_administrators_list',
     'house_staffers_list', 'journalists_list', 'non_dod_opm_staffers_list', 'regulation_commenters_list',
     'senate_staffers_list', 'thirty_under_thirty_list', 'whitehouse_staffers_list',
     'wikipedia_list', 'ar_staffers_list', 'ca_staffers_list', 'ct_staffers_list',
     'fl_staffers_list', 'ga_staffers_list', 'id_staffers_list', 'ks_staffers_list',
     'ky_staffers_list', 'ma_staffers_list', 'md_staffers_list', 'mi_staffers_list',
     'mn_staffers_list', 'mo_staffers_list', 'mt_staffers_list', 'nc_staffers_list',
     'nd_staffers_list', 'nh_staffers_list', 'nj_staffers_list', 'nm_staffers_list',
     'oh_staffers_list', 'ri_staffers_list', 'sc_staffers_list', 'tn_staffers_list',
     'tx_staffers_list', 'vt_staffers_list', 'wa_staffers_list', 'ak_contributions_list',
     'ca_contributions_list', 'ct_contributions_list', 'de_contributions_list',
     'fl_contributions_list', 'id_contributions_list', 'ky_contributions_list',
     'ma_contributions_list', 'md_contributions_list', 'ms_contributions_list',
     'nc_contributions_list', 'nj_contributions_list', 'nm_contributions_list',
     'oh_contributions_list', 'ok_contributions_list', 'tn_contributions_list',
     'tx_contributions_list', 'ut_contributions_list', 'vt_contributions_list',
     'fl_lobbyists_list', 'ky_lobbyists_list', 'mi_lobbyists_list', 'mo_lobbyists_list',
     'nc_lobbyists_list', 'oh_lobbyists_list', 'tn_lobbyists_list', 'tx_lobbyists_list',
     'ad_hoc_list', 'federal_level', 'state_level', 'local_level', 'donor', 'health_policy',
     'health_provider', 'health_insurance', 'pharma', 'other_insurance', 'professional', 'services',
     'government', 'democrat', 'republican', 'lobbying', 'politics', 'technology',
     'manufacturing', 'media', 'finance', 'energy', 'education', 'legal', 'environment',
     'community_social', 'national_security', 'sports', 'business', 'entertainment',
     'executive', 'legislative', 'all_business', 'all_government', 'healthcare', 'city', 'demo_county_name', 
     'msa', 'national_influence_rank', 'state_influence_rank'
]

filter_options = {
    'state': ['AK', 'AL' 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 
    'IN', 'IA', 'KS', 'KY', 'LA', 'MA', 'ME', 'MD', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE',
    'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 
    'VA', 'VT', 'WA', 'WI', 'WV', 'WY'],
    'gender': ['Female', 'Male', 'Other'],
    'demo_age_bucket_full': ['a18to29', 'b30to39', 'c40to49', 'd50to64', 'e65plus'],
    'demo_income_bucket_full': ['Income 00-30k', 'Income 030-50k', 'Income 050-75k', 'Income 075k-125', 'Income 125k+', 'unknown'],
    'demo_combined_ethnicity_4way': ['A', 'H', 'W', 'B'],
    'democrat': [0,1],
    'republican': [0,1],
    "influence": [0, 1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600],
    'national_influence_rank': [0, 0.01, 0.02, 0.03, 0.04, 0.07, 0.08, 0.1, 0.11, 0.14, 0.15, 0.17, 0.19, 0.25, 0.26, 0.28, 0.31, 0.32, 0.35, 0.36, 0.37, 0.52, 0.53, 0.54, 0.58, 0.59, 0.6, 0.61, 0.69, 0.7, 0.71, 0.72, 0.73, 0.74, 0.75, 0.76, 0.77, 0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1]
}

column_formats = {
	"first_name": "{}".format,
	"last_name": "{}".format,
	"state": "{}".format,
	"influence": lambda influence: "Extremely Influential" if influence > 100 else "Very Influential" if influence > 10 else "Influential",
	"contribution_amnt": "${:,}".format,
    "salary": "${:,}".format,
	"media_market": lambda media_market: "Anchorage, AK" if media_market == "anchorage ak" else "Mobile, AL-Pensacola, FL" if media_market == "mobile al-pensacola (ft. walton beach) fl" else "Montgomery, AL" if media_market == "montgomery (selma) al" else "Jonesboro, AR" if media_market == "jonesboro ar" else "Yuma, AZ" if media_market == "yuma az-el centro ca" else "Palm Springs, CA" if media_market == "palm springs ca" else "Bakersfield, CA" if media_market == "bakersfield ca" else "Washington, DC" if media_market == "washington dc (hagerstown md)" else "Boston, MA" if media_market == "boston ma (manchester nh)" else "Colorado Springs, CO" if media_market == "colorado springs-pueblo co" else "Tampa-St. Petersburg, FL" if media_market == "tampa-st.petersburg (sarasota) fl" else "Gainesville, FL" if media_market == "gainesville fl" else "Greenville-Spartanburg SC-Asheville, NC" if media_market == "greenville-spartanburg sc-asheville nc-anderson sc" else "Springfield-Decatur, IL" if media_market == "champaign & springfield-decatur il" else "Austin, TX" if media_market == "austin tx" else "Indianapolis, IN" if media_market == "indianapolis in" else "Springfield-Holyoke, MA" if media_market == "springfield-holyoke ma" else "Detroit, MI" if media_market == "detroit mi" else "Traverse City-Cadillac, MI" if media_market == "traverse city-cadillac mi" else "Lansing, MI" if media_market == "lansing mi" else "Duluth MN" if media_market == "duluth mn-superior wi" else "Green Bay-Appleton, WI" if media_market == "green bay-appleton wi" else "La Crosse-Eau Claire, WI" if media_market == "la crosse-eau claire wi" else "Butte-Bozeman, MT" if media_market == "butte-bozeman mt" else "Minot-Bismarck-Dickinson, ND" if media_market == "minot-bismarck-dickinson nd" else "Watertown, NY" if media_market == "watertown ny" else "Wichita Falls TX & Lawton, OK" if media_market == "wichita falls tx & lawton ok" else "Yakima-Pasco-Richland-Kennewick, WA" if media_market == "yakima-pasco-richland-kennewick wa" else "Harlingen-Weslaco-Brownsville-McAllen, TX" if media_market == "harlingen-weslaco-brownsville-mcallen tx" else "Harrisonburg, VA" if media_market == "harrisonburg va" else "Bluefield-Beckley-Oak Hill, WV" if media_market == "bluefield-beckley-oak hill wv" else "Juneau, AK" if media_market == "juneau ak" else "Huntsville-Decatur, AL" if media_market == "huntsville-decatur (florence) al" else "Shreveport, LA" if media_market == "shreveport la" else "Chico-Redding, CA" if media_market == "chico-redding ca" else "Chicago, IL" if media_market == "chicago il" else "Charlotte, NC" if media_market == "charlotte nc" else "Topeka, KS" if media_market == "topeka ks" else "Columbia-Jefferson city, MO" if media_market == "columbia-jefferson city mo" else "Greensboro-Winston Salem, NC" if media_market == "greensboro-high point-winston salem nc" else "Norfolk-Portsmouth-Newport News, VA" if media_market == "norfolk-portsmouth-newport news va" else "Harrisburg-Lancaster-Lebanon-York, PA" if media_market == "harrisburg-lancaster-lebanon-york pa" else "Erie, PA" if media_market == "erie pa" else "Oklahoma City, OK" if media_market == "oklahoma city ok" else "Eugene, OR" if media_market == "eugene or" else "Jackson, TN" if media_market == "jackson tn" else "Laredo, TX" if media_market == "laredo tx" else "Madison, WI" if media_market == "madison wi" else "Springfield, MO" if media_market == "springfield mo" else "Tucson, AZ" if media_market == "tucson (sierra vista) az" else "San Francisco-Oakland, CA" if media_market == "san francisco-oakland-san jose ca" else "Monterey-Salinas, CA" if media_market == "monterey-salinas ca" else "Denver, CO" if media_market == "denver co" else "West Palm Beach, FL" if media_market == "west palm beach-fort pierce fl" else "Tallahassee, FL" if media_market == "tallahassee fl-thomasville ga" else "Baton Rouge, LA" if media_market == "baton rouge la" else "Macon, GA" if media_market == "macon ga" else "Omaha, NE" if media_market == "omaha ne" else "St. Louis, MO" if media_market == "st. louis mo" else "Evansville, IN" if media_market == "evansville in" else "Lafayette, IN" if media_market == "lafayette in" else "Cincinnati, OH" if media_market == "cincinnati oh" else "Grand Rapids-Kalamazoo, MI" if media_market == "grand rapids-kalamazoo-battle creek mi" else "Minneapolis-St. paul, MN" if media_market == "minneapolis-st. paul mn" else "Bangor, ME" if media_market == "bangor me" else "Hattiesburg-Laurel, MS" if media_market == "hattiesburg-laurel ms" else "Jackson, MS" if media_market == "jackson ms" else "Billings, MT" if media_market == "billings mt" else "Great Falls, MT" if media_market == "great falls mt" else "Raleigh-Durham, NC" if media_market == "raleigh-durham (fayetteville) nc" else "Dayton, OH" if media_market == "dayton oh" else "Roanoke-Lynchburg, VA" if media_market == "roanoke-lynchburg va" else "Fairbanks, AK" if media_market == "fairbanks ak" else "Atlanta, GA" if media_market == "atlanta ga" else "Dallas-Ft. worth, TX" if media_market == "dallas-ft.worth tx" else "Medford-Klamath falls, OR" if media_market == "medford-klamath falls or" else "New York, NY" if media_market == "new york ny" else "Las Vegas, NV" if media_market == "las vegas nv" else "Spokane, WA" if media_market == "spokane wa" else "Louisville, KY" if media_market == "louisville ky" else "Portland-Auburn, ME" if media_market == "portland-auburn me" else "Marquette, MI" if media_market == "marquette mi" else "Helena, MT" if media_market == "helena mt" else "Rochester, NY" if media_market == "rochester ny" else "Buffalo, NY" if media_market == "buffalo ny" else "Tyler-Longview, TX" if media_market == "tyler-longview (lufkin & nacogdoches) tx" else "Clarksburg-Weston, WV" if media_market == "clarksburg-weston wv" else "Little Rock, AR" if media_market == "little rock-pine bluff ar" else "Phoenix, AZ" if media_market == "phoenix (prescott) az" else "Hartford-New Haven, CT" if media_market == "hartford & new haven ct" else "Philadelphia, PA" if media_market == "philadelphia pa" else "Orlando-Daytona Beach, FL" if media_market == "orlando-daytona beach-melbourne fl" else "Jacksonville, FL" if media_market == "jacksonville fl" else "Davenport I" if media_market == "davenport ia-rock island-moline il" else "Rochester MN" if media_market == "rochester mn-mason cityia-austin mn" else "Ft. Wayne, IN" if media_market == "ft. wayne in" else "Joplin MO-Pittsburg, KS" if media_market == "joplin mo-pittsburg ks" else "Baltimore, MD" if media_market == "baltimore md" else "Toledo, OH" if media_market == "toledo oh" else "Fargo-Valley city, ND" if media_market == "fargo-valley city nd" else "Mankato, MN" if media_market == "mankato mn" else "Greenwood-Greenville, MS" if media_market == "greenwood-greenville ms" else "Glendive, MT" if media_market == "glendive mt" else "Greenville-New Bern, NC" if media_market == "greenville-new bern-washington nc" else "Charleston, SC" if media_market == "charleston sc" else "Odessa-Midland, TX" if media_market == "odessa-midland tx" else "Richmond-Petersburg, VA" if media_market == "richmond-petersburg va" else "Lima, OH" if media_market == "lima oh" else "Sherman, TX" if media_market == "sherman tx-ada ok" else "Portland, OR" if media_market == "portland or" else "Wilkes Barre-Scranton, PA" if media_market == "wilkes barre-scranton pa" else "Beaumont-Port Arthur, TX" if media_market == "beaumont-port arthur tx" else "Seattle-Tacoma, WA" if media_market == "seattle-tacoma wa" else "Birmingham, AL" if media_market == "birmingham (anniston & tuscaloosa) al" else "Panama City, FL" if media_market == "panama city fl" else "New Orleans, LA" if media_market == "new orleans la" else "Twin Falls, ID" if media_market == "twin falls id" else "Salt Lake city, UT" if media_market == "salt lake city ut" else "Albany-Schenectady, NY" if media_market == "albany-schenectady-troy ny" else "Myrtle Beach, SC" if media_market == "myrtle beach-florence sc" else "North Platte, NE" if media_market == "north platte ne" else "Binghamton, NY" if media_market == "binghamton ny" else "Cleveland-Akron, OH" if media_market == "cleveland-akron (canton) oh" else "Youngstown, OH" if media_market == "youngstown oh" else "Johnstown-Altoona, PA" if media_market == "johnstown-altoona pa" else "Columbia, SC" if media_market == "columbia sc" else "Corpus Christi, TX" if media_market == "corpus christi tx" else "Abilene-Sweetwater, TX" if media_market == "abilene-sweetwater tx" else "Columbus, GA" if media_market == "columbus ga" else "Monroe, LA-El Dorado, AR" if media_market == "monroe la-el dorado ar" else "Los Angeles, CA" if media_market == "los angeles ca" else "Santa Barbara, CA" if media_market == "santa barbara-santa maria-san luis obispo ca" else "Savannah, GA" if media_market == "savannah ga" else "Chattanooga, TN" if media_market == "chattanooga tn" else "Cedar Rapids-Iowa City-Dubuque, IA" if media_market == "cedar rapids-waterloo-iowa city & dubuque ia" else "Ottumwaia-Kirksville, MO" if media_market == "ottumwaia-kirksville mo" else "Wausau-Rhinelander, WI" if media_market == "wausau-rhinelander wi" else "St. Joseph, MO" if media_market == "st. joseph mo" else "Bowling Green, KY" if media_market == "bowling green ky" else "Milwaukee, WI" if media_market == "milwaukee wi" else "Alexandria, LA" if media_market == "alexandria la" else "Missoula, MT" if media_market == "missoula mt" else "Wilmington, NC" if media_market == "wilmington nc" else "El Paso, TX" if media_market == "el paso tx (las cruces nm)" else "Utica, NY" if media_market == "utica ny" else "Waco-Temple, TX" if media_market == "waco-temple-bryan tx" else "Casper-Riverton, WY" if media_market == "casper-riverton wy" else "Dothan, AL" if media_market == "dothan al" else "Grand Junction-Montrose, CO" if media_market == "grand junction-montrose co" else "Ft. Myers-Naples, FL" if media_market == "ft. myers-naples fl" else "Albany, GA" if media_market == "albany ga" else "Honolulu, HI" if media_market == "honolulu hi" else "Idaho Falls-Pocatello, ID" if media_market == "idaho falls-pocatello id" else "Boise, ID" if media_market == "boise id" else "Knoxville, TN" if media_market == "knoxville tn" else "South Bend-Elkhart, IN" if media_market == "south bend-elkhart in" else "Tulsa, OK" if media_market == "tulsa ok" else "Lake Charles, LA" if media_market == "lake charles la" else "Lafayette, LA" if media_market == "lafayette la" else "Providenceri-New Bedford, MA" if media_market == "providenceri-new bedford ma" else "Syracuse, NY" if media_market == "syracuse ny" else "Presque Isle, ME" if media_market == "presque isle me" else "Burlington VT-plattsburgh, NY" if media_market == "burlington vt-plattsburgh ny" else "Elmira, NY" if media_market == "elmira (corning) ny" else "Columbus, OH" if media_market == "columbus oh" else "Zanesville, OH" if media_market == "zanesville oh" else "Wheeling WV-Steubenville, OH" if media_market == "wheeling wv-steubenville oh" else "Lubbock, TX" if media_market == "lubbock tx" else "Columbus-Tupelo, MS" if media_market == "columbus-tupelo-west point ms" else "Sacramento-Stockton-Modesto, CA" if media_market == "sacramento-stockton-modesto ca" else "Eureka, CA" if media_market == "eureka ca" else "San Diego, CA" if media_market == "san diego ca" else "Reno, NV" if media_market == "reno nv" else "Salisbury, MD" if media_market == "salisbury md" else "Wichita-Hutchinson, KS" if media_market == "wichita-hutchinson ks" else "Augusta, GA" if media_market == "augusta ga" else "Houston, TX" if media_market == "houston tx" else "Sioux City, IA" if media_market == "sioux city ia" else "Terre Haute, IN" if media_market == "terre haute in" else "Peoria-Bloomington, IL" if media_market == "peoria-bloomington il" else "Lincoln, NE" if media_market == "lincoln & hastings-kearney ne" else "Lexington, KY" if media_market == "lexington ky" else "Rapid City, SD" if media_market == "rapid city sd" else "Cheyenne, WY" if media_market == "cheyenne wy-scottsbluff ne" else "Amarillo, TX" if media_market == "amarillo tx" else "Victoria, TX" if media_market == "victoria tx" else "Charlottesville, VA" if media_market == "charlottesville va" else "Meridian, MS" if media_market == "meridian ms" else "Ft. Smith-Fayetteville, AR" if media_market == "ft. smith-fayetteville-springdale-rogers ar" else "Memphis, TN" if media_market == "memphis tn" else "Albuquerque-Santa Fe, NM" if media_market == "albuquerque-santa fe nm" else "Fresno-Visalia, CA" if media_market == "fresno-visalia ca" else "Bend, OR" if media_market == "bend or" else "Nashville, TN" if media_market == "nashville tn" else "Miami-Ft. Lauderdale, FL" if media_market == "miami-ft. lauderdale fl" else "Des Moines-Ames, IA" if media_market == "des moines-ames ia" else "Quincyil-Hannibal, MO" if media_market == "quincyil-hannibal mo-keokuk ia" else "Sioux Falls, SD" if media_market == "sioux falls (mitchell) sd" else "Paducah, KY-Cape Girardeau, MO" if media_market == "paducah ky-cape girardeau mo-harrisburg il" else "Rockford, IL" if media_market == "rockford il" else "Pittsburgh, PA" if media_market == "pittsburgh pa" else "Kansas City, MO" if media_market == "kansas city mo" else "Charleston-Huntington, WV" if media_market == "charleston-huntington wv" else "Tri-Cities, TN-VA" if media_market == "tri-cities tn-va" else "Flint-Saginaw, MI" if media_market == "flint-saginaw-bay city mi" else "Alpena, MI" if media_market == "alpena mi" else "Biloxi-Gulfport, MS" if media_market == "biloxi-gulfport ms" else "Parkersburg, WV" if media_market == "parkersburg wv" else "San Antonio, TX" if media_market == "san antonio tx" else "San Angelo, TX" if media_market == "san angelo tx" else "--",
	"healthcare": lambda healthcare: "Yes" if healthcare == 1 else "No" if healthcare == 0 else "Unknown",
	"government": lambda government: "Yes" if government == 1 else "No" if government == 0 else "Unknown",
	"business": lambda business: "Yes" if business == 1 else "No" if business == 0 else "Unknown",
    "national_influence": lambda cont: "{:02.1f}".format(cont),
    "national_influence_rank": lambda cont: "{:02.1f}".format(cont * 100),
    "state_influence": lambda cont: "{:02.1f}".format(cont * 100),
    "mobile_contact": lambda cont: "{:02.1f}".format(cont * 100),
	"digital_contact": lambda cont: "{:02.1f}".format(cont * 100),
	"c_bl_partisan_score": lambda score: "Strong Republican" if score <= .20 else "Lean Republican" if score <= .40 else "Moderate" if score <= .60 else "Lean Democrat" if score <= .80 else "Strong Democrat",
	"tv_any": lambda cont: "{:02.1f}".format(cont * 100),
	"children": lambda children: "Yes" if children == 1 else "No" if children == 0 else "Unknown",
    "spouse": lambda x: "Yes" if x == 1 else "No" if x == 0 else "Unknown",
    "count": "{:,}".format,
    "pct": lambda cont: "{:02.1f}%".format(cont * 100),
    "avg_contribution": "${:,}".format,
    "avg_salary": "${:,}".format,
    "influence_score": "{:,.1f}".format,
    "avg_influence_score": "{:,.1f}".format,
    "avg_influence_rank": lambda cont: "{:02.1f}".format(cont * 100),
    "avg_national_influence_rank": lambda cont: "{:02.1f}".format(cont * 100),
    "avg_state_influence_rank": lambda cont: "{:02.1f}".format(cont * 100),
    "avg_mail_contactability": lambda cont: "{:02.1f}".format(cont * 100),
    "avg_digital_contactability": lambda cont: "{:02.1f}".format(cont * 100),
    "avg_mobile_contactability": lambda cont: "{:02.1f}".format(cont * 100),
    "avg_tv_contactability": lambda cont: "{:02.1f}".format(cont * 100),
    "avg_partisan_score": lambda cont: "{:02.1f}".format(cont * 100),
    "pct_govt": lambda cont: "{:02.1f}%".format(cont * 1),
    "pct_business": lambda cont: "{:02.1f}%".format(cont * 1),
    "pct_female": lambda cont: "{:02.1f}%".format(cont * 1),
    "pct18to29": lambda cont: "{:02.1f}%".format(cont * 1),
    "pct30to39": lambda cont: "{:02.1f}%".format(cont * 1),
    "pct40to49": lambda cont: "{:02.1f}%".format(cont * 1),
    "pct50to64": lambda cont: "{:02.1f}%".format(cont * 1),
    "pct65plus": lambda cont: "{:02.1f}%".format(cont * 1),
}

media_market_def = '''CASE
WHEN media_market ilike 'Ancorage, AK' THEN 'anchorage ak'
WHEN media_market ilike 'Mobile, AL-Pensacola, FL' THEN 'mobile al-pensacola (ft. walton beach) fl'
WHEN media_market ilike 'Montgomery, AL' THEN 'montgomery (selma) al'
WHEN media_market ilike 'Jonesboro, AR' THEN 'jonesboro ar'
WHEN media_market ilike 'Yuma, AZ' THEN 'yuma az-el centro ca'
WHEN media_market ilike 'Palm Springs, CA' THEN 'palm springs ca'
WHEN media_market ilike 'Bakersfield, CA' THEN 'bakersfield ca'
WHEN media_market ilike 'Washington, DC' THEN 'washington dc (hagerstown md)'
WHEN media_market ilike 'Boston, MA' THEN 'boston ma (manchester nh)'
WHEN media_market ilike 'Colorado Springs, CO' THEN 'colorado springs-pueblo co'
WHEN media_market ilike 'Tampa-St. Petersburg, FL' THEN 'tampa-st.petersburg (sarasota) fl'
WHEN media_market ilike 'Gainesville, FL' THEN 'gainesville fl'
WHEN media_market ilike 'Greenville-Spartanburg SC-Asheville, NC' THEN 'greenville-spartanburg sc-asheville nc-anderson sc'
WHEN media_market ilike 'Springfield-Decatur, IL' THEN 'champaign & springfield-decatur il'
WHEN media_market ilike 'Austin, TX' THEN 'austin tx'
WHEN media_market ilike 'Indianapolis, IN' THEN 'indianapolis in'
WHEN media_market ilike 'Springfield-Holyoke, MA' THEN 'springfield-holyoke ma'
WHEN media_market ilike 'Detroit, MI' THEN 'detroit mi'
WHEN media_market ilike 'Traverse City-Cadillac, MI' THEN 'traverse city-cadillac mi'
WHEN media_market ilike 'Lansing, MI' THEN 'lansing mi'
WHEN media_market ilike 'Duluth MN' THEN 'duluth mn-superior wi'
WHEN media_market ilike 'Green Bay-Appleton, WI' THEN 'green bay-appleton wi'
WHEN media_market ilike 'La Crosse-Eau Claire, WI' THEN 'la crosse-eau claire wi'
WHEN media_market ilike 'Butte-Bozeman, MT' THEN 'butte-bozeman mt'
WHEN media_market ilike 'Minot-Bismarck-Dickinson, ND' THEN 'minot-bismarck-dickinson nd'
WHEN media_market ilike 'Watertown, NY' THEN 'watertown ny'
WHEN media_market ilike 'Wichita Falls TX & Lawton, OK' THEN 'wichita falls tx & lawton ok'
WHEN media_market ilike 'Yakima-Pasco-Richland-Kennewick, WA' THEN 'yakima-pasco-richland-kennewick wa'
WHEN media_market ilike 'Harlingen-Weslaco-Brownsville-McAllen, TX' THEN 'harlingen-weslaco-brownsville-mcallen tx'
WHEN media_market ilike 'Harrisonburg, VA' THEN 'harrisonburg va'
WHEN media_market ilike 'Bluefield-Beckley-Oak Hill, WV' THEN 'bluefield-beckley-oak hill wv'
WHEN media_market ilike 'Juneau, AK' THEN 'juneau ak'
WHEN media_market ilike 'Huntsville-Decatur, AL' THEN 'huntsville-decatur (florence) al'
WHEN media_market ilike 'Shreveport, LA' THEN 'shreveport la'
WHEN media_market ilike 'Chico-Redding, CA' THEN 'chico-redding ca'
WHEN media_market ilike 'Chicago, IL' THEN 'chicago il'
WHEN media_market ilike 'Charlotte, NC' THEN 'charlotte nc'
WHEN media_market ilike 'Topeka, KS' THEN 'topeka ks'
WHEN media_market ilike 'Columbia-Jefferson city, MO' THEN 'columbia-jefferson city mo'
WHEN media_market ilike 'Greensboro-Winston Salem, NC' THEN 'greensboro-high point-winston salem nc'
WHEN media_market ilike 'Norfolk-Portsmouth-Newport News, VA' THEN 'norfolk-portsmouth-newport news va'
WHEN media_market ilike 'Harrisburg-Lancaster-Lebanon-York, PA' THEN 'harrisburg-lancaster-lebanon-york pa'
WHEN media_market ilike 'Erie, PA' THEN 'erie pa'
WHEN media_market ilike 'Oklahoma City, OK' THEN 'oklahoma city ok'
WHEN media_market ilike 'Eugene, OR' THEN 'eugene or'
WHEN media_market ilike 'Jackson, TN' THEN 'jackson tn'
WHEN media_market ilike 'Laredo, TX' THEN 'laredo tx'
WHEN media_market ilike 'Madison, WI' THEN 'madison wi'
WHEN media_market ilike 'Springfield, MO' THEN 'springfield mo'
WHEN media_market ilike 'Tucson, AZ' THEN 'tucson (sierra vista) az'
WHEN media_market ilike 'San Francisco-Oakland, CA' THEN 'san francisco-oakland-san jose ca'
WHEN media_market ilike 'Monterey-Salinas, CA' THEN 'monterey-salinas ca'
WHEN media_market ilike 'Denver, CO' THEN 'denver co'
WHEN media_market ilike 'West Palm Beach, FL' THEN 'west palm beach-fort pierce fl'
WHEN media_market ilike 'Tallahassee, FL' THEN 'tallahassee fl-thomasville ga'
WHEN media_market ilike 'Baton Rouge, LA' THEN 'baton rouge la'
WHEN media_market ilike 'Macon, GA' THEN 'macon ga'
WHEN media_market ilike 'Omaha, NE' THEN 'omaha ne'
WHEN media_market ilike 'St. Louis, MO' THEN 'st. louis mo'
WHEN media_market ilike 'Evansville, IN' THEN 'evansville in'
WHEN media_market ilike 'Lafayette, IN' THEN 'lafayette in'
WHEN media_market ilike 'Cincinnati, OH' THEN 'cincinnati oh'
WHEN media_market ilike 'Grand Rapids-Kalamazoo, MI' THEN 'grand rapids-kalamazoo-battle creek mi'
WHEN media_market ilike 'Minneapolis-St. paul, MN' THEN 'minneapolis-st. paul mn'
WHEN media_market ilike 'Bangor, ME' THEN 'bangor me'
WHEN media_market ilike 'Hattiesburg-Laurel, MS' THEN 'hattiesburg-laurel ms'
WHEN media_market ilike 'Jackson, MS' THEN 'jackson ms'
WHEN media_market ilike 'Billings, MT' THEN 'billings mt'
WHEN media_market ilike 'Great Falls, MT' THEN 'great falls mt'
WHEN media_market ilike 'Raleigh-Durham, NC' THEN 'raleigh-durham (fayetteville) nc'
WHEN media_market ilike 'Dayton, OH' THEN 'dayton oh'
WHEN media_market ilike 'Roanoke-Lynchburg, VA' THEN 'roanoke-lynchburg va'
WHEN media_market ilike 'Fairbanks, AK' THEN 'fairbanks ak'
WHEN media_market ilike 'Atlanta, GA' THEN 'atlanta ga'
WHEN media_market ilike 'Dallas-Ft. worth, TX' THEN 'dallas-ft.worth tx'
WHEN media_market ilike 'Medford-Klamath falls, OR' THEN 'medford-klamath falls or'
WHEN media_market ilike 'New York, NY' THEN 'new york ny'
WHEN media_market ilike 'Las Vegas, NV' THEN 'las vegas nv'
WHEN media_market ilike 'Spokane, WA' THEN 'spokane wa'
WHEN media_market ilike 'Louisville, KY' THEN 'louisville ky'
WHEN media_market ilike 'Portland-Auburn, ME' THEN 'portland-auburn me'
WHEN media_market ilike 'Marquette, MI' THEN 'marquette mi'
WHEN media_market ilike 'Helena, MT' THEN 'helena mt'
WHEN media_market ilike 'Rochester, NY' THEN 'rochester ny'
WHEN media_market ilike 'Buffalo, NY' THEN 'buffalo ny'
WHEN media_market ilike 'Tyler-Longview, TX' THEN 'tyler-longview (lufkin & nacogdoches) tx'
WHEN media_market ilike 'Clarksburg-Weston, WV' THEN 'clarksburg-weston wv'
WHEN media_market ilike 'Little Rock, AR' THEN 'little rock-pine bluff ar'
WHEN media_market ilike 'Phoenix, AZ' THEN 'phoenix (prescott) az'
WHEN media_market ilike 'Hartford-New Haven, CT' THEN 'hartford & new haven ct'
WHEN media_market ilike 'Philadelphia, PA' THEN 'philadelphia pa'
WHEN media_market ilike 'Orlando-Daytona Beach, FL' THEN 'orlando-daytona beach-melbourne fl'
WHEN media_market ilike 'Jacksonville, FL' THEN 'jacksonville fl'
WHEN media_market ilike 'Davenport I' THEN 'davenport ia-rock island-moline il'
WHEN media_market ilike 'Rochester MN' THEN 'rochester mn-mason cityia-austin mn'
WHEN media_market ilike 'Ft. Wayne, IN' THEN 'ft. wayne in'
WHEN media_market ilike 'Joplin MO-Pittsburg, KS' THEN 'joplin mo-pittsburg ks'
WHEN media_market ilike 'Baltimore, MD' THEN 'baltimore md'
WHEN media_market ilike 'Toledo, OH' THEN 'toledo oh'
WHEN media_market ilike 'Fargo-Valley city, ND' THEN 'fargo-valley city nd'
WHEN media_market ilike 'Mankato, MN' THEN 'mankato mn'
WHEN media_market ilike 'Greenwood-Greenville, MS' THEN 'greenwood-greenville ms'
WHEN media_market ilike 'Glendive, MT' THEN 'glendive mt'
WHEN media_market ilike 'Greenville-New Bern, NC' THEN 'greenville-new bern-washington nc'
WHEN media_market ilike 'Charleston, SC' THEN 'charleston sc'
WHEN media_market ilike 'Odessa-Midland, TX' THEN 'odessa-midland tx'
WHEN media_market ilike 'Richmond-Petersburg, VA' THEN 'richmond-petersburg va'
WHEN media_market ilike 'Lima, OH' THEN 'lima oh'
WHEN media_market ilike 'Sherman, TX' THEN 'sherman tx-ada ok'
WHEN media_market ilike 'Portland, OR' THEN 'portland or'
WHEN media_market ilike 'Wilkes Barre-Scranton, PA' THEN 'wilkes barre-scranton pa'
WHEN media_market ilike 'Beaumont-Port Arthur, TX' THEN 'beaumont-port arthur tx'
WHEN media_market ilike 'Seattle-Tacoma, WA' THEN 'seattle-tacoma wa'
WHEN media_market ilike 'Birmingham, AL' THEN 'birmingham (anniston & tuscaloosa) al'
WHEN media_market ilike 'Panama City, FL' THEN 'panama city fl'
WHEN media_market ilike 'New Orleans, LA' THEN 'new orleans la'
WHEN media_market ilike 'Twin Falls, ID' THEN 'twin falls id'
WHEN media_market ilike 'Salt Lake city, UT' THEN 'salt lake city ut'
WHEN media_market ilike 'Albany-Schenectady, NY' THEN 'albany-schenectady-troy ny'
WHEN media_market ilike 'Myrtle Beach, SC' THEN 'myrtle beach-florence sc'
WHEN media_market ilike 'North Platte, NE' THEN 'north platte ne'
WHEN media_market ilike 'Binghamton, NY' THEN 'binghamton ny'
WHEN media_market ilike 'Cleveland-Akron, OH' THEN 'cleveland-akron (canton) oh'
WHEN media_market ilike 'Youngstown, OH' THEN 'youngstown oh'
WHEN media_market ilike 'Johnstown-Altoona, PA' THEN 'johnstown-altoona pa'
WHEN media_market ilike 'Columbia, SC' THEN 'columbia sc'
WHEN media_market ilike 'Corpus Christi, TX' THEN 'corpus christi tx'
WHEN media_market ilike 'Abilene-Sweetwater, TX' THEN 'abilene-sweetwater tx'
WHEN media_market ilike 'Columbus, GA' THEN 'columbus ga'
WHEN media_market ilike 'Monroe, LA-El Dorado, AR' THEN 'monroe la-el dorado ar'
WHEN media_market ilike 'Los Angeles, CA' THEN 'los angeles ca'
WHEN media_market ilike 'Santa Barbara, CA' THEN 'santa barbara-santa maria-san luis obispo ca'
WHEN media_market ilike 'Savannah, GA' THEN 'savannah ga'
WHEN media_market ilike 'Chattanooga, TN' THEN 'chattanooga tn'
WHEN media_market ilike 'Cedar Rapids-Iowa City-Dubuque, IA' THEN 'cedar rapids-waterloo-iowa city & dubuque ia'
WHEN media_market ilike 'Ottumwaia-Kirksville, MO' THEN 'ottumwaia-kirksville mo'
WHEN media_market ilike 'Wausau-Rhinelander, WI' THEN 'wausau-rhinelander wi'
WHEN media_market ilike 'St. Joseph, MO' THEN 'st. joseph mo'
WHEN media_market ilike 'Bowling Green, KY' THEN 'bowling green ky'
WHEN media_market ilike 'Milwaukee, WI' THEN 'milwaukee wi'
WHEN media_market ilike 'Alexandria, LA' THEN 'alexandria la'
WHEN media_market ilike 'Missoula, MT' THEN 'missoula mt'
WHEN media_market ilike 'Wilmington, NC' THEN 'wilmington nc'
WHEN media_market ilike 'El Paso, TX' THEN 'el paso tx (las cruces nm)'
WHEN media_market ilike 'Utica, NY' THEN 'utica ny'
WHEN media_market ilike 'Waco-Temple, TX' THEN 'waco-temple-bryan tx'
WHEN media_market ilike 'Casper-Riverton, WY' THEN 'casper-riverton wy'
WHEN media_market ilike 'Dothan, AL' THEN 'dothan al'
WHEN media_market ilike 'Grand Junction-Montrose, CO' THEN 'grand junction-montrose co'
WHEN media_market ilike 'Ft. Myers-Naples, FL' THEN 'ft. myers-naples fl'
WHEN media_market ilike 'Albany, GA' THEN 'albany ga'
WHEN media_market ilike 'Honolulu, HI' THEN 'honolulu hi'
WHEN media_market ilike 'Idaho Falls-Pocatello, ID' THEN 'idaho falls-pocatello id'
WHEN media_market ilike 'Boise, ID' THEN 'boise id'
WHEN media_market ilike 'Knoxville, TN' THEN 'knoxville tn'
WHEN media_market ilike 'South Bend-Elkhart, IN' THEN 'south bend-elkhart in'
WHEN media_market ilike 'Tulsa, OK' THEN 'tulsa ok'
WHEN media_market ilike 'Lake Charles, LA' THEN 'lake charles la'
WHEN media_market ilike 'Lafayette, LA' THEN 'lafayette la'
WHEN media_market ilike 'Providenceri-New Bedford, MA' THEN 'providenceri-new bedford ma'
WHEN media_market ilike 'Syracuse, NY' THEN 'syracuse ny'
WHEN media_market ilike 'Presque Isle, ME' THEN 'presque isle me'
WHEN media_market ilike 'Burlington VT-plattsburgh, NY' THEN 'burlington vt-plattsburgh ny'
WHEN media_market ilike 'Elmira, NY' THEN 'elmira (corning) ny'
WHEN media_market ilike 'Columbus, OH' THEN 'columbus oh'
WHEN media_market ilike 'Zanesville, OH' THEN 'zanesville oh'
WHEN media_market ilike 'Wheeling WV-Steubenville, OH' THEN 'wheeling wv-steubenville oh'
WHEN media_market ilike 'Lubbock, TX' THEN 'lubbock tx'
WHEN media_market ilike 'Columbus-Tupelo, MS' THEN 'columbus-tupelo-west point ms'
WHEN media_market ilike 'Sacramento-Stockton-Modesto, CA' THEN 'sacramento-stockton-modesto ca'
WHEN media_market ilike 'Eureka, CA' THEN 'eureka ca'
WHEN media_market ilike 'San Diego, CA' THEN 'san diego ca'
WHEN media_market ilike 'Reno, NV' THEN 'reno nv'
WHEN media_market ilike 'Salisbury, MD' THEN 'salisbury md'
WHEN media_market ilike 'Wichita-Hutchinson, KS' THEN 'wichita-hutchinson ks'
WHEN media_market ilike 'Augusta, GA' THEN 'augusta ga'
WHEN media_market ilike 'Houston, TX' THEN 'houston tx'
WHEN media_market ilike 'Sioux City, IA' THEN 'sioux city ia'
WHEN media_market ilike 'Terre Haute, IN' THEN 'terre haute in'
WHEN media_market ilike 'Peoria-Bloomington, IL' THEN 'peoria-bloomington il'
WHEN media_market ilike 'Lincoln, NE' THEN 'lincoln & hastings-kearney ne'
WHEN media_market ilike 'Lexington, KY' THEN 'lexington ky'
WHEN media_market ilike 'Rapid City, SD' THEN 'rapid city sd'
WHEN media_market ilike 'Cheyenne, WY' THEN 'cheyenne wy-scottsbluff ne'
WHEN media_market ilike 'Amarillo, TX' THEN 'amarillo tx'
WHEN media_market ilike 'Victoria, TX' THEN 'victoria tx'
WHEN media_market ilike 'Charlottesville, VA' THEN 'charlottesville va'
WHEN media_market ilike 'Meridian, MS' THEN 'meridian ms'
WHEN media_market ilike 'Ft. Smith-Fayetteville, AR' THEN 'ft. smith-fayetteville-springdale-rogers ar'
WHEN media_market ilike 'Memphis, TN' THEN 'memphis tn'
WHEN media_market ilike 'Albuquerque-Santa Fe, NM' THEN 'albuquerque-santa fe nm'
WHEN media_market ilike 'Fresno-Visalia, CA' THEN 'fresno-visalia ca'
WHEN media_market ilike 'Bend, OR' THEN 'bend or'
WHEN media_market ilike 'Nashville, TN' THEN 'nashville tn'
WHEN media_market ilike 'Miami-Ft. Lauderdale, FL' THEN 'miami-ft. lauderdale fl'
WHEN media_market ilike 'Des Moines-Ames, IA' THEN 'des moines-ames ia'
WHEN media_market ilike 'Quincyil-Hannibal, MO' THEN 'quincyil-hannibal mo-keokuk ia'
WHEN media_market ilike 'Sioux Falls, SD' THEN 'sioux falls (mitchell) sd'
WHEN media_market ilike 'Paducah, KY-Cape Girardeau, MO' THEN 'paducah ky-cape girardeau mo-harrisburg il'
WHEN media_market ilike 'Rockford, IL' THEN 'rockford il'
WHEN media_market ilike 'Pittsburgh, PA' THEN 'pittsburgh pa'
WHEN media_market ilike 'Kansas City, MO' THEN 'kansas city mo'
WHEN media_market ilike 'Charleston-Huntington, WV' THEN 'charleston-huntington wv'
WHEN media_market ilike 'Tri-Cities, TN-VA' THEN 'tri-cities tn-va'
WHEN media_market ilike 'Flint-Saginaw, MI' THEN 'flint-saginaw-bay city mi'
WHEN media_market ilike 'Alpena, MI' THEN 'alpena mi'
WHEN media_market ilike 'Biloxi-Gulfport, MS' THEN 'biloxi-gulfport ms'
WHEN media_market ilike 'Parkersburg, WV' THEN 'parkersburg wv'
WHEN media_market ilike 'San Antonio, TX' THEN 'san antonio tx'
WHEN media_market ilike 'San Angelo, TX' THEN 'san angelo tx' END as media_market'''