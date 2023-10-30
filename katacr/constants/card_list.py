"""
2023/10/30: Total card numbers: 116
"""
elixir2card = {
  1: [
    'skeletons',
    'skeletons-evolution',
    'electro-spirit',
    'fire-spirit',
    'ice-spirit',
    'heal-spirit',
  ],
  2: [
    'goblins',
    'spear-goblins',
    'bomber',
    'bats',
    'bats-evolution',
    'zap',
    'giant-snowball',
    'ice-golem',
    'barbarian-barrel',
    'wall-breakers',
    'rage',
    'the-log',
  ],
  3: [
    'archers',
    'arrows',
    'knight',
    'knight-evolution',
    'minions',
    'cannon',
    'goblin-gang',
    'skeleton-barrel',
    'firecracker',
    'firecracker-evolution',
    'royal-delivery',
    'tombstone',
    'mega-minion',
    'dart-goblin',
    'earthquake',
    'elixir-golem',
    'goblin-barrel',
    'guards',
    'skeleton-army',
    'clone',
    'tornado',
    'miner',
    'princess',
    'ice-wizard',
    'royal-ghost',
    'bandit',
    'fisherman',
  ],
  4: [
    'skeleton-dragons',
    'mortar',
    'mortar-evolution',
    'tesla',
    'fireball',
    'mini-pekka',
    'musketeer',
    'goblin-cage',
    'valkyrie',
    'battle-ram',
    'bomb-tower',
    'flying-machine',
    'hog-rider',
    'battle-healer',
    'furnace',
    'zappies',
    'baby-dragon',
    'dark-prince',
    'freeze',
    'poison',
    'hunter',
    'goblin-drill',
    'electro-wizard',
    'inferno-dragon',
    'phoenix',
    'magic-archer',
    'lumberjack',
    'night-witch',
    'mother-witch',
    'golden-knight',
    'skeleton-king',
    'mighty-miner',
  ],
  5: [
    'barbarians',
    'barbarians-evolution',
    'minion-horde',
    'rascals',
    'giant',
    'goblin-hut',
    'inferno-tower',
    'wizard',
    'royal-hogs',
    'witch',
    'balloon',
    'prince',
    'electro-dragon',
    'bowler',
    'executioner',
    'cannon-cart',
    'ram-rider',
    'graveyard',
    'archer-queen',
    'monk',
  ],
  6: [
    'royal-giant',
    'royal-giant-evolution',
    'elite-barbarians',
    'rocket',
    'barbarian-hut',
    'elixir-collector',
    'giant-skeleton',
    'lightning',
    'goblin-giant',
    'x-bow',
    'sparky',
  ],
  7: [
    'royal-recruits',
    'royal-recruits-evolution',
    'pekka',
    'electro-giant',
    'mega-knight',
    'lava-hound',
  ],
  8: [
    'golem',
  ],
  9: [
    'three-musketeers',
  ],
  10: []
}

card2elixir = {
  'skeletons': 1,
  'skeletons-evolution': 1,
  'electro-spirit': 1,
  'fire-spirit': 1,
  'ice-spirit': 1,
  'heal-spirit': 1,
  'goblins': 2,
  'spear-goblins': 2,
  'bomber': 2,
  'bats': 2,
  'bats-evolution': 2,
  'zap': 2,
  'giant-snowball': 2,
  'ice-golem': 2,
  'barbarian-barrel': 2,
  'wall-breakers': 2,
  'rage': 2,
  'the-log': 2,
  'archers': 3,
  'arrows': 3,
  'knight': 3,
  'knight-evolution': 3,
  'minions': 3,
  'cannon': 3,
  'goblin-gang': 3,
  'skeleton-barrel': 3,
  'firecracker': 3,
  'firecracker-evolution': 3,
  'royal-delivery': 3,
  'tombstone': 3,
  'mega-minion': 3,
  'dart-goblin': 3,
  'earthquake': 3,
  'elixir-golem': 3,
  'goblin-barrel': 3,
  'guards': 3,
  'skeleton-army': 3,
  'clone': 3,
  'tornado': 3,
  'miner': 3,
  'princess': 3,
  'ice-wizard': 3,
  'royal-ghost': 3,
  'bandit': 3,
  'fisherman': 3,
  'skeleton-dragons': 4,
  'mortar': 4,
  'mortar-evolution': 4,
  'tesla': 4,
  'fireball': 4,
  'mini-pekka': 4,
  'musketeer': 4,
  'goblin-cage': 4,
  'valkyrie': 4,
  'battle-ram': 4,
  'bomb-tower': 4,
  'flying-machine': 4,
  'hog-rider': 4,
  'battle-healer': 4,
  'furnace': 4,
  'zappies': 4,
  'baby-dragon': 4,
  'dark-prince': 4,
  'freeze': 4,
  'poison': 4,
  'hunter': 4,
  'goblin-drill': 4,
  'electro-wizard': 4,
  'inferno-dragon': 4,
  'phoenix': 4,
  'magic-archer': 4,
  'lumberjack': 4,
  'night-witch': 4,
  'mother-witch': 4,
  'golden-knight': 4,
  'skeleton-king': 4,
  'mighty-miner': 4,
  'barbarians': 5,
  'barbarians-evolution': 5,
  'minion-horde': 5,
  'rascals': 5,
  'giant': 5,
  'goblin-hut': 5,
  'inferno-tower': 5,
  'wizard': 5,
  'royal-hogs': 5,
  'witch': 5,
  'balloon': 5,
  'prince': 5,
  'electro-dragon': 5,
  'bowler': 5,
  'executioner': 5,
  'cannon-cart': 5,
  'ram-rider': 5,
  'graveyard': 5,
  'archer-queen': 5,
  'monk': 5,
  'royal-giant': 6,
  'royal-giant-evolution': 6,
  'elite-barbarians': 6,
  'rocket': 6,
  'barbarian-hut': 6,
  'elixir-collector': 6,
  'giant-skeleton': 6,
  'lightning': 6,
  'goblin-giant': 6,
  'x-bow': 6,
  'sparky': 6,
  'royal-recruits': 7,
  'royal-recruits-evolution': 7,
  'pekka': 7,
  'electro-giant': 7,
  'mega-knight': 7,
  'lava-hound': 7,
  'golem': 8,
  'three-musketeers': 9,
}

card_list = ['skeletons', 'skeletons-evolution', 'electro-spirit', 'fire-spirit', 'ice-spirit', 'heal-spirit', 'goblins', 'spear-goblins', 'bomber', 'bats', 'bats-evolution', 'zap', 'giant-snowball', 'ice-golem', 'barbarian-barrel', 'wall-breakers', 'rage', 'the-log', 'archers', 'arrows', 'knight', 'knight-evolution', 'minions', 'cannon', 'goblin-gang', 'skeleton-barrel', 'firecracker', 'firecracker-evolution', 'royal-delivery', 'tombstone', 'mega-minion', 'dart-goblin', 'earthquake', 'elixir-golem', 'goblin-barrel', 'guards', 'skeleton-army', 'clone', 'tornado', 'miner', 'princess', 'ice-wizard', 'royal-ghost', 'bandit', 'fisherman', 'skeleton-dragons', 'mortar', 'mortar-evolution', 'tesla', 'fireball', 'mini-pekka', 'musketeer', 'goblin-cage', 'valkyrie', 'battle-ram', 'bomb-tower', 'flying-machine', 'hog-rider', 'battle-healer', 'furnace', 'zappies', 'baby-dragon', 'dark-prince', 'freeze', 'poison', 'hunter', 'goblin-drill', 'electro-wizard', 'inferno-dragon', 'phoenix', 'magic-archer', 'lumberjack', 'night-witch', 'mother-witch', 'golden-knight', 'skeleton-king', 'mighty-miner', 'barbarians', 'barbarians-evolution', 'minion-horde', 'rascals', 'giant', 'goblin-hut', 'inferno-tower', 'wizard', 'royal-hogs', 'witch', 'balloon', 'prince', 'electro-dragon', 'bowler', 'executioner', 'cannon-cart', 'ram-rider', 'graveyard', 'archer-queen', 'monk', 'royal-giant', 'royal-giant-evolution', 'elite-barbarians', 'rocket', 'barbarian-hut', 'elixir-collector', 'giant-skeleton', 'lightning', 'goblin-giant', 'x-bow', 'sparky', 'royal-recruits', 'royal-recruits-evolution', 'pekka', 'electro-giant', 'mega-knight', 'lava-hound', 'golem', 'three-musketeers']