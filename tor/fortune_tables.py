from .tor_dice_roller import gandalf, eye

fortune_table = {
    eye: "The Eye of the Enemy focuses elsewhere.<br>Decrease Eye Awareness by 1.",
    1: "You may bypass a threat without attracting notice",
    2: "You gain the attention of a potential ally",
    3: "An enemy inadvertently reveals their position",
    4: "You gain favoured ground",
    5: "Enemies run afoul of danger",
    6: "You locate or learn of a useful item",
    7: "Your success instils new hope or renewed resolve",
    8: "You find a moment of comfort or safety",
    9: "You learn or realize something which gives helpful insight into your mission",
    10: "You encounter an opportunity suited to your nature or abilities",
    gandalf: "An unexpected ally appears or sends aid",
}

ill_fortune_table = {
    eye: "Your actions catch the Eye of the Enemy.<br>Increase Eye Awareness by 2.",
    1: "You draw unwanted attention",
    2: "Your actions are observed by someone of ill-intent",
    3: "Unexpected enemies emerge or are sighted",
    4: "You are hindered by difficult terrain or an unfavourable environment",
    5: "You find yourself ill-equipped for the circumstances",
    6: "A favoured weapon or item is lost, broken, or sacrificed",
    7: "You are plagued by troubling visions or thoughts",
    8: "An old injury or stress resurfaces",
    9: "You learn or realize something which adds a new complication to your mission",
    10: "You face a test which is contrary to your nature or abilities",
    gandalf: "An ally becomes a hindrance or liability",
}
