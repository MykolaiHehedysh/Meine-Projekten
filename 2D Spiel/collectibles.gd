extends Node2D

var apple = preload("res://collectebless/gold.tscn")


func _on_timer_timeout() -> void:
	var appleTemp = apple.instantiate()
	var rng = RandomNumberGenerator.new()
	var randint = randf_range(830,2250)
	appleTemp.position = Vector2 (randint,400)
	add_child(appleTemp)
