namespace Content.Server.Chat.Systems;

using Content.Shared.Chat.Prototypes;
using Content.Shared.Damage;
using Robust.Shared.Prototypes;
using Robust.Shared.Random;
using Robust.Shared.Timing;
using Robust.Shared.Utility;

public sealed class EmoteOnDamageSystem : EntitySystem
{
    [Dependency] private readonly IGameTiming _gameTiming = default!;
    [Dependency] private readonly IPrototypeManager _prototypeManager = default!;
    [Dependency] private readonly IRobustRandom _random = default!;
    [Dependency] private readonly ChatSystem _chatSystem = default!;

    public override void Initialize()
    {
        base.Initialize();

        SubscribeLocalEvent<EmoteOnDamageComponent, EntityUnpausedEvent>(OnUnpaused);
        SubscribeLocalEvent<EmoteOnDamageComponent, DamageChangedEvent>(OnDamage);
    }

    private void OnUnpaused(EntityUid uid, EmoteOnDamageComponent emoteOnDamage, ref EntityUnpausedEvent args)
    {
        emoteOnDamage.LastEmoteTime += args.PausedTime;
    }

    private void OnDamage(EntityUid uid, EmoteOnDamageComponent emoteOnDamage, DamageChangedEvent args)
    {
        if (!args.DamageIncreased)
            return;

        if (emoteOnDamage.LastEmoteTime + emoteOnDamage.EmoteCooldown > _gameTiming.CurTime)
            return;

        if (emoteOnDamage.Emotes.Count == 0)
            return;

        if (!_random.Prob(emoteOnDamage.EmoteChance))
            return;

        var emote = _random.Pick(emoteOnDamage.Emotes);
        if (emoteOnDamage.WithChat)
        {
            _chatSystem.TryEmoteWithChat(uid, emote, emoteOnDamage.HiddenFromChatWindow);
        }
        else
        {
            _chatSystem.TryEmoteWithoutChat(uid,emote);
        }

        emoteOnDamage.LastEmoteTime = _gameTiming.CurTime;
    }

    /// <summary>
    /// Try to add an emote to the entity, which will be performed at an interval.
    /// </summary>
    public bool AddEmote(EntityUid uid, string emotePrototypeId, EmoteOnDamageComponent? emoteOnDamage = null)
    {
        if (!Resolve(uid, ref emoteOnDamage, logMissing: false))
            return false;

        DebugTools.Assert(_prototypeManager.HasIndex<EmotePrototype>(emotePrototypeId), "Prototype not found. Did you make a typo?");

        return emoteOnDamage.Emotes.Add(emotePrototypeId);
    }

    /// <summary>
    /// Stop preforming an emote.
    /// </summary>
    public bool RemoveEmote(EntityUid uid, string emotePrototypeId, EmoteOnDamageComponent? emoteOnDamage = null)
    {
        if (!Resolve(uid, ref emoteOnDamage, logMissing: false))
            return false;

        DebugTools.Assert(_prototypeManager.HasIndex<EmotePrototype>(emotePrototypeId), "Prototype not found. Did you make a typo?");

        return emoteOnDamage.Emotes.Remove(emotePrototypeId);
    }
}
