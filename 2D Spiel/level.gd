extends Node2D
@onready var light = $DirectionalLight2D
@onready var pointlight  =$PointLight2D
@onready var day_text = $"CanvasLayer/Day text"
@onready var animPlayer = $CanvasLayer/AnimationPlayer
var alive = true
enum {
	MORNING,
	DAY,
	EVENING,
	NIGHT
}
var state = MORNING
var day_count:int
func _ready():
	light.enabled = true
	day_count= 1
	set_day_text()
	day_text_fade()
	
	
func day_text_fade ():	
	animPlayer.play ( "day_text_fade_in")
	await get_tree().create_timer(3).timeout
	animPlayer.play("day_text_fade_out")

func _process(delta: float) -> void:
	match state:
		MORNING:
			_morning_state()
		EVENING:
			_evening_state()
			
func _morning_state ():
	var tween = get_tree().create_tween()
	tween.tween_property(light, "energy",0.0, 20)
	
func _evening_state ():
	var tween = get_tree().create_tween()
	tween.tween_property(light, "energy",0.98, 20)				
		
		

func _on_day_night_timeout() -> void:
	if state < 3:
		
		state += 1
	else:
		state = MORNING
		day_count += 1	
		set_day_text()
		animPlayer.play("day_text_fade_in")
		await get_tree().create_timer(3).timeout
		animPlayer.play("day_text_fade_out")
		

			
		
		
		
		
func set_day_text ():
	day_text.text = "DAY" + str(day_count)		
		
		 
func death():
	alive = false
	get_tree().change_scene_to_file("res://menu.tscn")


func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.name == "player":
		if alive == true: 
			body.health -= 100
			death()
			
			
		
