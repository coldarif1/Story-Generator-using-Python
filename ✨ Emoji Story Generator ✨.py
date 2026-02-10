# Importing random module
import random

# Defining list of phrases which will help to build a story

Sentence_starter = ['📝✨🚀🌌🌟', '👩‍🚀🛸🌍💫🌈', '🌻🌍🏞️🧚‍♀️🌊🌅🍃❤️']
character        = [' 🧑‍🎤🎸✨',' 🌟🏆🤩', ' 🚀💫🎉🎶🌈❤️']
time             = [' ⏳🕰️🔄🌀🌍🌌🎇📆📅🌟👶➡️👦👴🕰️💫🌈🌌🕊️💭💫', ' ⏳🕰️🔄🌀🌍🌌🎇📆📅🌟👶➡️👦👴🕰️💫🌈🌌🕊️💭💫',
                    '🃏🎴🀄️🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚🕛🕜🕝🕞🕟🕠🕡🕢🕣🕤🕥🕦🕧']
story_plot       = [' 🦸‍♂️✨🌆🌌👾',' 🚀🛸⚔️💥🛡️🏙️🎉 ']

place            = [' 🗺️🏴‍☠️⛵🏝️🦜', ' 🔍💎👑🎉']
second_character = [' 🦦🦥🐁🐀🐿🦔🐾🐉🐲', ' 🦦🦥🐁🐀🐿🦔🐾🐉🐲']
age              = [' 👶➡️👦➡️👨➡️', ' 👴🌳💭😌🌅🌟']
work             = [' 👨‍💻💼🌍📊📈🤝💡', ' 🚀🔍📅⏳💪😓✨🏆']

# Selecting an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
      random.choice(time)+random.choice(story_plot) +
      random.choice(place)+random.choice(second_character)+
      random.choice(age)+random.choice(work))

#In the 20 BC there was a man named Jack. One full-moon night he was passing 
#by the garden he saw a young lady 
#who seemed very old and feeble searching something.

<script>
  // Greeting Logic
 function getGreetingParts(date = new Date()) {
  const h = date.getHours();
  if (h >= 5 && h < 12)   // Morning until 11:59 AM
      return { text: "Good Morning",  emoji: "🌅", sub: "Fresh start. Let’s get it!" };
  if (h >= 12 && h < 16)  // 12:00 PM - 3:59 PM
      return { text: "Good Afternoon", emoji: "🌤️", sub: "Keep up the momentum!" };
  if (h >= 16 && h < 20)  // 4:00 PM - 7:59 PM
      return { text: "Good Evening",   emoji: "🌇", sub: "You’re almost there—finish strong!" };
  return { text: "Good Night", emoji: "🌙", sub: "Wrap up and recharge for tomorrow." };
}


</script>

#📝✨🚀🌌🌟👩‍🚀🛸🌍💫🌈🌻🌍🏞️🧚‍♀️🌊🌅🍃❤️
#🦸‍♂️✨🌆🌌👾🚀🛸⚔️💥🛡️🏙️🎉
#https://emojistorygenerator.com/examples



