# You can use findNearestEnemy() on your soldiers to get their nearest enemy instead of yours

while True:

    friends = hero.findFriends()

    # Use for-loop and for each friend:
    for friend in friends:

        # If they see an enemy then command to attack.

        enemy = friend.findNearestEnemy()

        if enemy:

            hero.command(friend, "attack", enemy)

        # Command to move east by small steps.

        else:

            moveTo = {"x": friend.pos.x + 0.35, "y": friend.pos.y}

            hero.command(friend, "move", moveTo)

