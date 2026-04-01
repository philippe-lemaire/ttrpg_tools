town_law_generalities = """When creating a town, choose a law or two that sets it apart from its
neighbors. Obviously, a true town would have many laws, but a single
law in this game will often dramatically change play in that town. Don’t
apply too many laws at once. Let additional laws emerge as a result of
the players’ actions or town events.

Choose new laws from these lists or invent your own."""

town_law_types = ("Criminal", "Sumptuary", "Civil", "Religious")

criminal_laws = (
    "Begging is against the law. Punishable by transport.",
    "Cursing is a criminal act. Punishable by branding.",
    "Drunkenness is a criminal act. Punishable by public humiliation.",
    "Theft is a criminal act. Punishable by loss of a limb or facial branding.",
    "Using magic in town is a criminal act. Punishable by removal of tongue.",
    "Dueling is a criminal act. Punishable by loss of dueling hand.",
    "Brawling is a criminal act. Punishable by public humiliation.",
    "Riding ahead of your betters is a criminal act. Punishable by whipping.",
    "Praying to any Immortal is a criminal act. Punishable by branding or execution.",
    "Sedition is a criminal act. Punishable by incarceration or execution.",
    "Defaming the ruling class is a criminal act. Punishable by incarceration or whipping.",
    "Belonging to any cult is a criminal act. Punishable by execution.",
    "Failing to report for watch duty is a criminal act. Punishable by whipping.",
)

sumptuary_laws = (
    "One may not wear fashionable shoes above one’s station.",
    "Punishable by three days in stocks or a fine (Ob 2 Resources).",
    "One may not wear fashionable clothes above one’s station.",
    "Punishable by three days in stocks or a fine (Ob 2 Resources).",
    "All magicians must wear conical hats. Failure to do so is punishable by whipping or a fine (Ob 3 Resources).",
    "All theurges must wear plain vestments. Failure to be properly robed is punishable by a fine (Ob 2 Resources).",
    "It is illegal for anyone but temple priests to bear relics.",
    "Punishable by loss of relic and three days in stocks.",
    "All residents may eat meat only once a week. Punishable by loss of meat and a fine (Ob 1 Resources).",
    "All families must have one boy child. Failure results in the arrest of the of the mother or father.",
    "All persons must wear a particular symbol or item of clothing. Punishable by three days in stocks and a fine (Ob 1 Resources).",
)

civil_laws = (
    "All persons are forbidden to bear arms greater than a knife or dagger in town. Punishable by confiscation of illegal arms and a fine (Ob 2 Resources test).",
    "Magicians may not testify before a judge. Punishable by execution.",
    "Contracts with the guild are annulled.",
    "Contracts with the guild are enforced and payable immediately.",
    "Temple priests are not subject to civil law.",
    "No wills written before today shall be enforced.",
    "All youths between the ages of 12 and 18 must train in a particular weapon. Failure to do so punishable by public humiliation.",
    "All guild members must stand watch for the remainder of the month. Failure to do so is punishable by whipping.",
    "Only temple priests are subject to religious law.",
    "Proclamation of war against distant neighbor.",
    "All marriage contracts are strictly enforced. Failure to honor a marriage contract is punishable by public humiliation.",
)

religious_laws = (
    "Only priests may officiate funerals, weddings and births.",
    "Punishable by a fine (Ob 3 Resources).",
    "Performing invocations is forbidden. Punishable by exile.",
    "All persons must observe a new holiday. The market and guild",
    "hall are closed. Failure to observe is punishable by flogging.",
    "Communicating with the excommunicated is forbidden.",
    "Punishable by stoning.",
    "Thence forth, today is a day of fasting. Failure to fast is punishable by flogging.",
    "Dwarves and halflings may not become friends. Punishable by whipping.",
    "Elves must cover their faces. Failure to hide one’s face is punishable by whipping.",
    "Elves may not share food. Punishable by whipping.",
    "One may not eat meat while the sun is up. Punishable by whipping.",
    "One may not drink water during the night. Punishable by whipping.",
    "Owning or drinking wine is forbidden. Punishable by whipping and confiscation of illegal stocks.",
    "Taking a life is forbidden. Punishable by retaliation or compensation.",
    "Touching a temple priest is forbidden. Punishable by public flogging.",
    "Taking an Immortal’s name in vain is forbidden. Punishable by public flogging.",
    "All persons must pay a tithe to the temple (equivalent to 1D of cash). Failure to pay punishable by whipping.",
    "Dwarves and elves may not walk together. Punishable by whipping.",
    "Crusade declared. All persons must enlist. Failure to enlist is punishable by fine (Ob 2 Resources).",
    "The temple priests declare that absolution from sin can be had at their hands. Absolution requires a donation (Ob 2 Resources). Sinners are publicly whipped.",
    "Defiling a tomb is an offense before the Immortals. Punishable by execution.",
    "Casting a spell upon another is forbidden. Punishable by execution.",
)

town_law_dict = {
    t: laws
    for t, laws in zip(
        town_law_types, (criminal_laws, sumptuary_laws, civil_laws, religious_laws)
    )
}
