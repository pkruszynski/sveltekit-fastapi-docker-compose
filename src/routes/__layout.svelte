<script>
    import "carbon-components-svelte/css/all.css";
    import {
        Theme,
        Header,
        HeaderUtilities,
        HeaderGlobalAction,
        HeaderNav,
        HeaderNavItem,
    } from "carbon-components-svelte";
    import ColorSwitch from "carbon-icons-svelte/lib/ColorSwitch.svelte";

    let theme = "g80";

    function changeTheme() {
        theme === "g80" ? (theme = "g10") : (theme = "g80");
    }
</script>

<Theme bind:theme />

<Header
    href="/"
    platformName="SvelteKit Carbon"
    persist
    persistKey="__carbon-theme"
>
    <HeaderNav>
        <HeaderNavItem href="/scores" text="Scores" />
        <HeaderNavItem href="/random_number" text="Random Number" />
    </HeaderNav>
    <HeaderUtilities>
        <HeaderGlobalAction
            aria-label="Switch Theme"
            icon={ColorSwitch}
            on:click={changeTheme}
        />
    </HeaderUtilities>
</Header>

<slot />
