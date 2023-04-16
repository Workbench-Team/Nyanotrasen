game-ticker-restart-round =  Перезапуск раунда...

game-ticker-start-round =  Раунд начинается...

game-ticker-start-round-cannot-start-game-mode-fallback =  Не удалось запустить режим { $failedGameMode }! Запускаем { $fallbackMode }...

game-ticker-start-round-cannot-start-game-mode-restart =  Не удалось запустить режим { $failedGameMode }! Перезапуск раунда...

game-ticker-unknown-role =  Неизвестный

game-ticker-delay-start =  Начало раунда было отложено на { $seconds } секунд.

game-ticker-pause-start =  Начало раунда было приостановлено.

game-ticker-pause-start-resumed =  Отсчет начала раунда возобновлен.

game-ticker-player-join-game-message =  Добро пожаловать на Космическую Станцию 14! Если вы играете впервые, обязательно нажмите ESC на клавиатуре и прочитайте правила игры, а также не бойтесь просить помощи в "Админ помощь".

game-ticker-get-info-text = 

Hi and welcome to [color = white]Space Station 14![/color]

The current round is: [color = white]#{ $roundId }[/color]

The current player count is: [color = white]{ $playerCount }[/color] ([color=white]{ $readyCount }[/color] { $readyCount ->
        [one] is
       *[other] are
    } ready)

The current map is: [color = white]{ $mapName }[/color]

The current game mode is: [color = white]{ $gmTitle }[/color]

>[color = yellow]{ $desc }[/color]

game-ticker-get-info-preround-text = 

game-ticker-no-map-selected =  [color=red]Карта не выбрана![/color]

game-ticker-player-no-jobs-available-when-joining =  При попытке присоединиться к игре ни одной роли не было доступно.
 При попытке присоединиться к игре ни одной роли не было доступно.

player-join-message =  Игрок { $name } присоединился.

player-first-join-message =  Игрок { $name } присоединился впервые.
 Игрок { $name } присоединился впервые.

player-leave-message =  Игрок { $name } покинул сервер.

latejoin-arrival-announcement = 
    { $character } ({ $job }) { $gender ->
        [male] прибыл
        [female] прибыла
        [epicene] прибыли
       *[neuter] прибыл
    } на станцию!

latejoin-arrival-sender =  Станции

