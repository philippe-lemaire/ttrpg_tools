from dataclasses import dataclass


biological_wounds_data = (
    (
        "0",
        "Knocked Out",
        "–",
        "CON save vs unconscious for d6 rounds.<br>While unconscious, all attacks automatically hit you.",
    ),
    (
        "-1",
        "Damaged Item",
        "–",
        "An item is damaged and is unusable until fixed.<br>Roll d20 to determine the item slot affected.",
    ),
    (
        "-2",
        "Bloody Mouth",
        "1",
        "Your mouth drools blood and your speech slurs.",
    ),
    (
        "-3",
        "Teeth Knocked Out",
        "1",
        "DIS on EGO Saves",
    ),
    (
        "-4",
        "Scrambled Nerves",
        "1",
        "DIS on PSY Saves",
    ),
    (
        "-5",
        "Addling Wound",
        "1",
        "DIS on INT Saves",
    ),
    (
        "-6",
        "Stomach Wound",
        "1",
        "DIS on CON Saves",
    ),
    (
        "-7",
        "Crippling Wound",
        "1",
        "DIS on DEX Saves",
    ),
    (
        "-8",
        "Weakening Wound",
        "1",
        "DIS on STR Saves",
    ),
    (
        "-9",
        "Bloody Gash",
        "1",
        "-d8 max HP.",
    ),
    (
        "-10",
        "Major Fracture",
        "2",
        "-d6 STR and -d6 DEX.",
    ),
    (
        "-11",
        "Lost an Eye",
        "2",
        "-d6 DEX and -d6 EGO.",
    ),
    (
        "-12",
        "Cracked Skull",
        "2",
        "-d8 INT and -d8 PSY. You pass out.",
    ),
    (
        "-13",
        "Mangled Guts",
        "2",
        "-d8 CON and -d10 max HP. You pass out.",
    ),
    (
        "-14",
        "Severed Hand",
        "2",
        "-d8 STR, -d8 DEX. You pass out.",
    ),
    (
        "-15",
        "Severed Arm",
        "3",
        "-10 STR, -10 DEX. You pass out.",
    ),
    (
        "-16",
        "Severed Leg",
        "3",
        "-10 STR, -10 DEX. You pass out.",
    ),
    (
        "-17",
        "Braindead",
        "3",
        "-10 INT, -10 PSY, -10 EGO. You pass out.",
    ),
    (
        "-18",
        "Bloody Mess",
        "3-9",
        "Roll 3 random Wounds using 3d6. You pass out.",
    ),
    (
        "-19",
        "Death’s Door",
        "5",
        "Any further damage is lethal until this wound is healed.<br>You pass out.",
    ),
    (
        "-20",
        "Fatality",
        "–",
        "You are dead.",
    ),
)


synthetic_wounds_data = (
    (
        "0",
        "Update Required",
        "–",
        "CON save vs unconscious for d6 rounds.<br>While unconscious, all attacks automatically hit you.",
    ),
    (
        "-1",
        "Damaged Item",
        "–",
        "An item is damaged and is unusable until fixed.<br>Roll d20 to determine the item slot affected.",
    ),
    (
        "-2",
        "Supercoolant Leak",
        "1",
        "You begin leaking supercoolant. You are Deprived and cannot regain HP until this Wound is fixed.",
    ),
    (
        "-3",
        "Ego-Engine Stutter",
        "1",
        "-d4 EGO.",
    ),
    (
        "-4",
        "Quantum-Reasoning Overflow",
        "1",
        "-d4 PSY",
    ),
    (
        "-5",
        "Memory Crystal Fracture",
        "1",
        "-d4 INT",
    ),
    (
        "-6",
        "Coolant Loop Overheat",
        "1",
        "-d4 CON",
    ),
    (
        "-7",
        "Kinesthetics Drive Failure",
        "1",
        "-d4 DEX",
    ),
    (
        "-8",
        "Limb Hydraulics Compromised",
        "1",
        "-d4 STR",
    ),
    (
        "-9",
        "Synthskin Damaged",
        "2",
        "-d4 AV. Suffer double damage.",
    ),
    (
        "-10",
        "Incompatible Motion Interface",
        "2",
        "A limb is no longer compatible with your core software. -d6 STR and -d6 DEX until fixed.",
    ),
    (
        "-11",
        "Personality Nexus Scrambled",
        "2",
        "Reroll INT, PSY and EGO scores. Your voice and personality are altered.",
    ),
    (
        "-12",
        "Vischip Disabled",
        "3",
        "You are blind. You cannot make ranged attacks and make melee attacks with DIS.",
    ),
    (
        "-13",
        "Cascading Kinesthetics Debilitation",
        "3",
        "Lose -2 STR and DEX per day.",
    ),
    (
        "-14",
        "Emotive Language Export Corruption",
        "4",
        "Your emotions and speech are encrypted and do not match what you intended to communicate.",
    ),
    (
        "-15",
        "Infinite Practical Memory Loop",
        "4",
        "You repeat your last action step by step for the next d6 hours.",
    ),
    (
        "-16",
        "Motive Drive Inhibited",
        "5",
        "- 10 STR, -10 DEX. -10 CON. You shut down for d6 hours.",
    ),
    (
        "-17",
        "Personality Nexus Damaged",
        "5",
        "-10 INT, -10 PSY, -10 EGO. You shut down for d6 hours.",
    ),
    (
        "-18",
        "Terminal Memory Crystal Corruption",
        "6",
        "You lose one Level and all XP. This loss is permanent, even when the Wound is fixed.",
    ),
    (
        "-19",
        "General Systems Failure",
        "–",
        "You are dead. If your Ego Engine is removed from your body, it can be installed in a new shell (see p.xx)",
    ),
    (
        "-20",
        "Ego-Engine Destroyed",
        "–",
        "You are dead. Your Ego Engine is damaged beyond repair and you cannot be rebooted.",
    ),
)


@dataclass
class Wound:
    hp: str
    name: str
    slots: str
    effect: str


biological_wounds = [Wound(*line) for line in biological_wounds_data]
synthetic_wounds = [Wound(*line) for line in synthetic_wounds_data]
