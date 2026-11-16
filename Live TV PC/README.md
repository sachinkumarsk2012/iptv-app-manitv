# Livewave for PC

Livewave is a Windows live TV guide and player. Extract the ZIP and double-click **Start Livewave.bat**. Python 3 and an internet connection are needed for online playlists and HLS playback. Keep the launcher window open while using the app; press Ctrl+C in it to stop the local server.

The app opens the last playlist or the Indian TV playlist. Use the playlist icon in the video panel to choose a playlist, add an M3U URL, or open an M3U file from the PC. FM and radio stations are filtered out. Some streams may be offline or may not allow browser playback.

At startup, the full-height channel bar stays open so you can choose a channel. After you tune a channel, playback fills the app window. Use the on-screen Channels button or G to open the channel bar; it closes after five seconds without activity while playing. The selected channel is highlighted. Press F for fullscreen, Space to play or pause, the left/right arrows to change channels, and the up/down arrows to adjust volume from 0 to 100. The date and clock include seconds. The playback bar has a volume slider.

DishTV custom numbers and categories from the supplied SD/HD workbook are applied to matching playlist channel names. Channel names are kept exactly as supplied by the playlist; unmatched channels keep their existing numbers and playlist categories.

Open **Settings** with the gear button. In **Channels**, switch between all channels and favorites, select a channel, then change its number, move it up/down, favorite it, hide it, or reset the order. The **Edit & manage** button on the guide opens the add/remove channel manager. Channel preferences and layout settings are saved in this PC's browser storage.

Settings also include picture adjustments, sound, display controls, language/category filters, playlist sources, and **UI Customize**. Adjust panel size, opacity, roundness, blur, animation, colors, visible guide rows, and background image. Changes preview immediately and save on this PC. Open the playlist panel to load one or more XMLTV URLs; comma-separate two feeds if needed. EPG programmes match channel IDs or display names.

## Sources

- Indian channels: https://raw.githubusercontent.com/iptv-org/iptv/master/streams/in.m3u
- News, sports, and kids playlists: https://iptv-org.github.io/iptv/categories/
- Playlist index: https://github.com/iptv-org/iptv/blob/master/PLAYLISTS.md


## Android TV, STB, or phone on the same Wi-Fi

1. Connect the Windows PC and Android TV/STB or phone to the same Wi-Fi network.
2. On the PC, double-click **Start Livewave TV or Mobile.bat**. Keep its window open.
3. On Windows, run `ipconfig` and find the PC's IPv4 Address (for example, `192.168.1.20`).
4. In the TV or phone browser, open `http://192.168.1.20:8765` using your PC's actual address. If Windows Firewall asks, allow access on Private networks.
5. Use the TV remote or phone screen to choose a channel. Streaming needs an internet connection; the phone's FM radio is not used.

This is a same-network browser run. To have Livewave appear as an installed app on the TV home screen, it needs an Android TV APK wrapper. Android TV apps need a TV launcher entry, and the web UI can be bundled in a WebView. See the official [Android TV app setup](https://developer.android.com/training/tv/get-started/create) and [WebView local content guide](https://developer.android.com/develop/ui/views/layout/webapps/load-local-content). An APK can later be installed with [Android Debug Bridge](https://developer.android.com/tools/adb).
