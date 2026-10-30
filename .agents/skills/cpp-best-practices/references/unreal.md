# C / C++ best practices: Unreal Engine 5

- Gameplay logic in C++ classes exposed to Blueprints (`UCLASS`, `UPROPERTY(EditAnywhere, BlueprintReadOnly)`, `UFUNCTION(BlueprintCallable)`), Blueprints for content and tuning; UE naming (`A` actors, `U` objects, `F` structs, `E` enums, `b` booleans), `TObjectPtr` for UObject members, never raw `new` for UObjects.
- Modules declared in `*.Build.cs`, Gameplay Ability System / Enhanced Input for new projects, data in Data Assets/Data Tables, automation tests (`IMPLEMENT_SIMPLE_AUTOMATION_TEST`) for logic.
