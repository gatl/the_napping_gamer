#!/usr/bin/env python3

# Copyright 2015, 2016 Gustavo Laboreiro
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.


###############################################################################
#                      THIS IS WHAT YOU NEED TO KNOW:
#
# How do you configure this program for your needs?
# Only two things are important: your country and your currency.
# If you don't care about the prices, ignore this part.
#
# You can also add a file called "wishlist.txt" to the script, containing
# part of the name of the game you seek. You will only be notified when those
# games show up.
# You can also set a maximum price, so that bad offers do not disturb you.
#
# Finally, if you do not want the browser popping up, turn it off at the end
# of the configuration section. The same goes with sound notifications.
#
# Below you will find the configuration entries.
#



# We only need to configure the country, due to regional prices.
# Not all combinations for country/currency can be found in our data source.

# We will set the currency first. Chose one of the following:
#
#  'AUD', 'EUR', 'GBP', 'RUB', 'USD'

currency_code = 'EUR'


# Next, what is your country two letters code?
# Possible values are:
#
#  'AD', 'AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AM', 'AN', 'AO', 'AR', 'AS',
#  'AT', 'AT', 'AU', 'AU', 'AW', 'AZ', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BE', 'BF',
#  'BG', 'BG', 'BH', 'BI', 'BJ', 'BL', 'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW',
#  'BY', 'BY', 'BZ', 'CA', 'CC', 'CD', 'CF', 'CH', 'CH', 'CI', 'CK', 'CL', 'CM',
#  'CN', 'CO', 'CP', 'CR', 'CU', 'CV', 'CX', 'CY', 'CY', 'CZ', 'CZ', 'DE', 'DE',
#  'DJ', 'DK', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EE', 'EG', 'EH', 'ER', 'ES',
#  'ES', 'ET', 'FI', 'FI', 'FJ', 'FK', 'FM', 'FO', 'FR', 'FR', 'GA', 'GB', 'GB',
#  'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP', 'GQ', 'GR', 'GR',
#  'GT', 'GU', 'GW', 'GY', 'HK', 'HN', 'HR', 'HR', 'HT', 'HU', 'HU', 'ID', 'IE',
#  'IE', 'IL', 'IM', 'IN', 'IO', 'IQ', 'IR', 'IS', 'IS', 'IT', 'IT', 'JE', 'JM',
#  'JO', 'JP', 'KE', 'KG', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP', 'KR', 'KW', 'KY',
#  'KZ', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LI', 'LK', 'LR', 'LS', 'LT', 'LT', 'LU',
#  'LU', 'LV', 'LV', 'LY', 'MA', 'MC', 'MC', 'MD', 'MD', 'ME', 'ME', 'MF', 'MG',
#  'MH', 'MK', 'ML', 'MM', 'MN', 'MO', 'MP', 'MQ', 'MR', 'MS', 'MT', 'MT', 'MU',
#  'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG', 'NI', 'NL', 'NL',
#  'NO', 'NO', 'NP', 'NR', 'NU', 'NZ', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PG', 'PH',
#  'PK', 'PL', 'PL', 'PM', 'PN', 'PR', 'PS', 'PT', 'PT', 'PW', 'PY', 'QA', 'RE',
#  'RO', 'RO', 'RS', 'RS', 'RU', 'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SE',
#  'SG', 'SH', 'SI', 'SI', 'SK', 'SK', 'SL', 'SM', 'SM', 'SN', 'SO', 'SR', 'ST',
#  'SV', 'SY', 'SZ', 'TC', 'TD', 'TG', 'TH', 'TJ', 'TJ', 'TK', 'TL', 'TM', 'TM',
#  'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US', 'UY', 'UZ',
#  'UZ', 'VA', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN', 'VU', 'WF', 'WS', 'XK', 'YE',
#  'YT', 'ZA', 'ZM', 'ZW',
#
# If you cannot find your contry here, use GOG's code 'REST'.

country_code = 'PT'


# If you have a wishlist, the script will only notify for games in it.
# The list will have one game per line, and is case insensitive.
# This is not a regular expression. We do a substring matching.
# Tell the script the name of the file here.
#
# The script will look for this file in your working directory.
# You can set it with a full path if you like.

wishlist_file = "wishlist.txt"


# How much money are you willing to pay for a game you want (in your currency)?

maximum_price = 99.99



# How to do the "new game" notification!

# Do you want to get your browser to open the page for the new game on sale?
# Valid values are: "True" and "False".

browser_notify = True


# If you have more than one browser, which one should be used?
# Valid names include 'firefox', 'google-chrome' and 'opera'.
# See full list at https://docs.python.org/3/library/webbrowser.html

browser_name = None


# How about making some noise?
# Valid values are: "True" and "False".

sound_notify = True


# Use a fancy sound (currently only on MS Windos).
# (Requires sound_notify enabled to have effect.)
# If set to False, just use a beeping sound.
# Valid values are: "True" and "False".

fancy_sound = True


# Use the eSpeak text-to-speech.
# Its website is at http://espeak.sourceforge.net/
# Please enter the full path of the "espeak" binary, or leave it empty
# (or set to None) to disable its use.
# This option currently is independent of sound_notify.

espeak_system = ""



# There is no need to change the rest of the code if you do not want to.




# This is the URL to GOG's "API".

url = "https://www.gog.com/insomnia/current_deal"


# Initial polling interval in seconds. This will be reduced when apropriate
# (e.g. a game pool is almost depleted it will reduce drasticaly).

sleep_time = 30


# Data about the games we already saw will be remembered.
# When we see a game, we store its information in here.

seen_games = dict()


import time
import urllib.request
import json
import os.path
import sys
import webbrowser
import subprocess



# This function provides the user notification for a new game just seen.
# A new process will be initiated, like a browser window, a music player or
# a desktop notification tool.
# One could also have the program just beep here and not fork.
# We pass along the information regarding the new game, incluing its GOG URL.

def provide_notification(game_info):
  "Notify the user that a new game is available in promotion."

  # Print the new entry.
  current_time = time.strftime("%H:%M:%S",time.localtime())
  notification_data = {"currency": currency_code, "time": current_time}
  notification_data.update(game_info)

  msg_format = '{time} NEW! "{title}"  '\
'at {currency} {local_discount_price:.2f} (-{price_discount:d}%)  '\
'{stock_left:d}/{total_stock:d} copies  {url}'
  msg_text = msg_format.format_map(notification_data)
  print(msg_text)


  # Before bothering the user, see if the game is worthwhile.
  wishlist_entry = game_relevance(game_info)
  # game_relevance outputs: True -> No Wishlist; False -> Irrelevant; string -> wishlist entry.
  if wishlist_entry and wishlist_entry is not True:
    print(' (Match found for "{}")'.format(wishlist_entry))
  elif wishlist_entry is False:
    return


  # This is supposed to be the URL used to purchase the game.
  # I hope I got it right. It seems to work, at least.

  purchase_url_fmt = "https://www.gog.com/"
  purchase_url = purchase_url_fmt.format(game_info) # Direct link not working.

  if browser_notify:
    webbrowser.get(browser_name).open(purchase_url, new=2, autoraise=True)


  # This is how we further notify the user that a new game is available.
  # The code is different for each platform.

  if sys.platform.startswith('linux') or sys.platform.startswith('freebsd'):

    # Use the "notify-send" to discreetly inform the user.

    try:
      title = "GOG"
      short_text_format = "{title}  {currency}\xa0{local_discount_price}\n{url}"
      short_text = short_text_format.format_map(notification_data)
      subprocess.call(["/usr/bin/notify-send", "--expire-time=10000",
          "--app-name=the_napping_gamer", title, short_text])
    except FileNotFoundError:
      pass

    if sound_notify:
      try:
        # Do not forget that beep needs to be SETUID to work.
        subprocess.call(["/usr/bin/beep"])
      except FileNotFoundError:
        pass

    if espeak_system:
      try:
        # eSpeak produces a lot of errors. We will hide its output.
        # Warning: this may mask some problem with the program.
        with open("/dev/null", "w") as blackhole:
          subprocess.call([espeak_system, game_info["title"]],
              stderr=blackhole)
      except FileNotFoundError:
        print("ERROR: Could not find espeak program: ", espeak_system, file=sys.stderr)



  elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
    if sound_notify:
      import winsound
      if fancy_sound:
        winsound.PlaySound(None, winsound.MB_ICONASTERISK)
      else:
        beep_repeats = 4
        for i in range(beep_repeats):
          winsound.Beep(1100,300)

    if espeak_system:
      try:
        subprocess.call([espeak_system, game_info["title"]])
      except FileNotFoundError:
        print("ERROR: Could not find espeak program: ", espeak_system, file=sys.stderr)



# Check to see if the game fits the price and if the name is in the wishlist.
# If the wishlist file is not present, assume that the user wants to see all
# games being offered.
# The list is checked at each run (that is, when something new appears). That
# way the list can be changed without the program being restarted.

def game_relevance(game_info):
  "Verify that the game meets the price criteria and if it is found in the \
wishlist. If there is no wishlist file, all games are relevant. \
Otherwise, check line in the wishlist file for a (case insensitive) substring \
of the current game title."

  if game_info["local_discount_price"] > maximum_price:
    return False
  try:
    with open(wishlist_file, "r") as wishlist:
      for entry in wishlist:
        cleaned_entry = entry.strip().lower()
        if cleaned_entry != "" and cleaned_entry in game_info["title"].lower():
          return entry.strip()
      else:
        return False
  except FileNotFoundError:
    return True



# Read the contents of the file at the URL provided. 
# If there is some communication difficulty, we retry once.
# The URL we are probing contains JSON data regarding the games on promotion.
# We return the parsed data as a Python object.

def read_from_url(url):
  "Read the JSON object stored at the URL provided."

  retry_wait_time = 5  # Retry after these many seconds on error.
  try:
    indata = urllib.request.urlopen(url)
  except urllib.error.HTTPError:
    time.sleep(retry_wait_time)
    print("(Network hickup.)", file=sys.stderr)
    indata = urllib.request.urlopen(url)
  bytes_data = indata.read()
  json_data = json.loads(bytes_data.decode())
  return json_data



# GOG stores the information about the game promotion in a structure containing
# lots of information that we need to parse (e.g. new price and discounted price),
# as well as prices in all currencies and countries.
# We parse this information, convert most of it to numbers and discard what is
# not needed.

def extract_game_data(data):
  "Parse GOG's data structure and return a simple unnested dictionary."

  # GOG uses a somewhat complex structure to handle prices, since it deals with
  # both regional prices and multiple currencies. Some currencies are considered
  # in multiple countries, and some countries allow for the use of multiple
  # currencies.
  # Furthermore, this is not fixed. One game may display a price in USD for
  # Europe while another one may have only EUR.

  # For the sake of efficiency, we should start by looking at the currency data,
  # as they provide lesse options. However, since it is easier for a user to
  # change their currency used than their location, we will work on the country
  # first and then work our way with the monetary unit.

  # We will not support alternate currencies in here, but doing it this way
  # makes this addition simpler to write.

  # GOG's prices are in a structure as follows:
  # {... "prices": {
  #       "c": {"3": <COUNTRY_LIST_3>, "1": <COUNTRY_LIST_1>, ...},
  #       "p": {"GBP": {"4":"1.39,6.69"}, "USD": {"3": "2.29,12.69",...} ... }
  #
  # <COUNTRY_LIST> means a list of country codes seperated by comma (as in
  # "DK,EE,FI,FR,DE,GR,HU,IS,IE,IT,LV,LI,LT,LU,MT,MC,M").
  # We can also see that the discounted price and full price are also comma
  # seperated. The keys "c" and "p" most likely stand for "country" and "price".

  # It is possible that a game costs X USD in one country and Y USD in another.
  # Once we know which number groups our country integrates, we'll look only at
  # them.

  def get_price_value(price_data):
    "From the GOG price data structure, extract only the prices matching the \
globally defined country and currency. Returns the tuple (discounted, full)."
    groups_using_currency = price_data["groupsPrices"][currency_code]
    for code in groups_using_currency:
      if country_code in price_data["countriesGroups"][code]:
        values = price_data["groupsPrices"][currency_code][code].split(";")
        return float(values[0]), float(values[1])
    else:
      print("country group index: {}, currency_values: {}".format(index, currency_values), price_data, sep="\n", file=sys.stderr)
      raise KeyError('Price value not found for country "{}"' \
                       ' (or rest of the world) and currency {}. Keys seen: {}'.format(
                         country_code, currency_code, ",".join(currency_values.keys())))


  # With the previous auxiliary functions, parsing the remaining data is trivial.
  # From the URL we do not get just the game info. There is also a variable called
  # "retryInterval" (with the value 1.5 at the moment). Thus, we verify that
  # we will work only on the dictionaries.
  #
  # We iterate across all games available. This means that it will work no
  # matter how many games are introduced for sale.

  url_format = "https://www.gog.com/{}"

  # We have two types of offers: bunles (multiple games) and products (single games).

  if data["dealType"] == "bundle":
    game_title = "{} ({})".format(data["bundle"]["title"], data["bundle"]["description"])
    local_discount_price = local_full_price = 0
    for product_id in data["bundle"]["productIds"]:
      prod_id_in_bundle = str(product_id)
      prod_local_full_price, prod_local_discount_price = get_price_value(data["bundle"]["prices"][prod_id_in_bundle])
      local_discount_price += prod_local_discount_price
      local_full_price += prod_local_full_price
    game_id = 0
    game_url = "https://www.gog.com/"
    game_image = data["bundle"]["image"],

  elif data["dealType"] == "product":
    game_title = data["product"]["title"]
    local_full_price, local_discount_price = get_price_value(data["product"]["prices"])
    game_id = int(data["product"]["id"]),
    game_url = url_format.format(data["product"]["url"]),
    game_image = data["product"]["image"],

  else:
    raise ValueError("Unknown deal type: {}.".format(data["dealType"]))
  return [{
    "title": game_title,
    "price_discount": int(data["discount"]),
    "stock_left": int(data["amountLeft"]),
    "total_stock": int(data["amountTotal"]),
    "local_discount_price": local_discount_price,
    "local_full_price": local_full_price,
    "id": game_id,
    "url": game_url,
    "image": game_image,
    "time_checked": time.time()}]


# It would be unpolite to be constantly hammering GOG's servers. For this
# reason we define polling intervals. Ideally we would inquiry GOG just after
# a new game is introduced.

def calculate_depletion_time(earliest_data, latest_data):
  "Given two data readings, calculate how many seconds untill all remaining \
units (present at the latest reading) are gone."
  stock_reduction = earliest_data["stock_left"] - latest_data["stock_left"]
  if stock_reduction <= 0:
    # No sale since the previous polling, or (and this is possible), the
    # number of games still available has gone up --- I assume this happens
    # when the sale of units does not carry through.
    return None
  else:
    earliest_time = earliest_data["time_checked"]
    latest_time = latest_data["time_checked"]
    time_interval = latest_time - earliest_time
    depletion_ratio = stock_reduction / time_interval
    depletion_time = latest_data["stock_left"] / depletion_ratio
    return int(depletion_time)



# Do the server polling.

def check_games():

  def time_fmt(time_value):
    "Translate time in seconds since epoch into a regular current time string."
    return time.strftime("%H:%M:%S", time.gmtime(time_value))

  # We will track how long we expect each game.
  all_delays = []
  avg_seconds_to_sell = 3  # How many seconds do we expect for a copy to sell?
  short_time = 15  # How many seconds is a short wait time?
  for game_info in extract_game_data(read_from_url(url)):
    game_id = game_info["id"]
    current_time = time.time()

    if game_id not in seen_games:

        # This is the first time we see this game. We cannot say yet how long
        # it will be available for sale.

      provide_notification(game_info)
      seen_games[game_id] = [game_info]
      all_delays.append(game_info["stock_left"] * avg_seconds_to_sell)
      print('{time}    "{title}"  {currency} {local_discount_price}  ' \
          '{stock_left}/{total_stock}'.format(
          time=time_fmt(current_time),
          currency=currency_code,
          **game_info))
    else:

        # Estimate how long the stock it will last, now that we have
        # two observations or more.
        # The long_estimate compares the first time we saw the game available
        # with the present.
        # The short estimate compares it with the last time we saw more units
        # for sale than we currently see (most often, the previous observation).

      long_time_estimate = calculate_depletion_time(seen_games[game_id][0], game_info)
      for i in range(len(seen_games[game_id])-1, -1, -1):
        if seen_games[game_id][i]["stock_left"] > game_info["stock_left"]:
          short_time_estimate = calculate_depletion_time(seen_games[game_id][i], game_info)
          current_delay = (long_time_estimate + short_time_estimate) / 2
          break
      else:
        short_time_estimate = None
        current_delay = None

      # Remember this observation only if it does not represent an odd event.
      if game_info["stock_left"] < seen_games[game_id][-1]["stock_left"]:
        seen_games[game_id].append(game_info)

      all_delays.append(current_delay)
      print('{time}    "{title}"  {currency} {local_discount_price}  ' \
          '{stock_left}/{total_stock} expected sale time: {delay} min ' \
          '({delay_time}))'.format(
          time=time_fmt(current_time),
          currency=currency_code,
          delay="{:.1f}".format(current_delay/60) if current_delay else "NA",
          delay_time=time_fmt(current_delay + current_time) if current_delay else "NA",
          **game_info))

  # How long do we expect to wait for the next poll?
  wait_time = int(min(filter(None,all_delays), default=sleep_time))
  if wait_time <= short_time:
    print("    No time to sleep!", end="  ")
  else:
    print("    You may nap for {:.1f} more minutes ({:s}). I'll stand guard!".format(
        wait_time/60, time_fmt(current_time + wait_time)), end="  ")

  return wait_time



if __name__ == "__main__":
  minimum_sleep_value = 2

  while True:
    wait_time = max(min(sleep_time, check_games()), minimum_sleep_value)
    print("Next peek in {} seconds.".format(wait_time))
    time.sleep(wait_time)
