emag-success =  Карточка замыкает что-то в { $target }.

emag-no-charges =  Не осталось зарядов!

emag-charges-remaining = 
    На нём имеется { $charges } { $charges ->
        [one] заряд
        [few] заряда
       *[other] зарядов
    }.

[one] It has [color = fuchsia]{ $charges }[/color] charge remaining.

*[other] It has [color = fuchsia]{ $charges }[/color] charges remaining.
    }

emag-max-charges =  Он имеет [color=green]максимум[/color] зарядов.

emag-recharging = 
    { $seconds ->

[one] There is [color = yellow]{ $seconds }[/color] second left until the next charge.

*[other] There are [color = yellow]{ $seconds }[/color] seconds left until the next charge.
    }

