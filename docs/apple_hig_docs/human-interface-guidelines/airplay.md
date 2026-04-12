# AirPlay

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/airplay

# AirPlay

AirPlayは、iOS、iPadOS、macOS、およびtvOSのデバイスからApple TV、HomePod、およびAirPlay対応のテレビやスピーカーにメディアコンテンツをワイヤレスでストリーミングできるテクノロジーです。

![AirPlayアイコンのスケッチ。画像の上に長方形と円形のグリッド線が重ねられており、画像全体が6色の初代Appleロゴの青色を連想させる青みを帯びています。](https://docs-assets.developer.apple.com/published/78c4958f93b91d6c753dc1d2e515e5ad/technologies-AirPlay-intro%402x.png)

## [ベストプラクティス](/jp/design/human-interface-guidelines/airplay#Best-practices)

**できる限りシステムが提供するメディアプレーヤーを使う。** ビルトインのメディアプレーヤーは、標準のコントロールセットを備え、チャプタナビゲーション、字幕、クローズドキャプション、AirPlayストリーミングなどの機能に対応しています。また、実装が容易で、システム全体で一貫した馴染みのある再生体験を提供し、ほとんどのメディアアプリのニーズに応えます。カスタムビデオプレーヤーの設計は、システムが提供するプレーヤーでアプリのニーズを満たせない場合にのみ検討してください。デベロッパ向けのガイダンスは、[`AVPlayerViewController`](/documentation/AVKit/AVPlayerViewController)を参照してください。

![システムが提供するメディアプレーヤーのスクリーンショット。ビデオの再生中に一時停止しています。](https://docs-assets.developer.apple.com/published/f6ea036a0e6db3780504adc3c8afece4/airplay-video-screen%402x.png)

**コンテンツを可能な限り高い解像度で提供する。**[HTTP Live Streaming](https://developer.apple.com/documentation/http-live-streaming)（HLS）プレイリストには、ユーザが使っているデバイスに適した解像度でコンテンツを体験できるように、用意できる解像度をすべて含める必要があります（AVFoundationがデバイスに基づいて解像度を自動的に選択します）。提供されている解像度に不足があると、デバイスで本来再生できるはずの解像度よりも低い画質でストリーミングされることになります。例えば、iPhoneの720pでは見栄えに問題がなくても、AirPlayで4Kテレビにストリーミングしたときに画質が低くなる、といった問題が起きてしまいます。

**ユーザが期待するコンテンツだけをストリーミングする。** アプリ自体のコンテキスト内でしか意味を持たないバックグラウンドループやショートビデオなどのコンテンツをストリーミングすることは控えます。デベロッパ向けのガイダンスは、[`usesExternalPlaybackWhileExternalScreenIsActive`](/documentation/AVFoundation/AVPlayer/usesExternalPlaybackWhileExternalScreenIsActive)を参照してください。

**AirPlayストリーミングとAirPlayミラーリングの両方に対応する。** 両方の機能に対応すると、ユーザに最大限の柔軟性を提供できます。

**リモートコントロールイベントに対応する。** リモートコントロールイベントに対応すると、ロック画面や、Siriとの会話、HomePodの操作で、再生、一時停止、早送りなどのアクションを選択できるようになります。デベロッパ向けのガイダンスは、[リモートコマンドセンターのイベント](/documentation/MediaPlayer/remote-command-center-events)を参照してください。

**アプリがバックグラウンドに移動したりデバイスがロックされたりしても再生を停止しない。** 例えば、ユーザはアプリからストリーミングを開始したテレビ番組の再生がメールの確認中やデバイスをスリープ状態にしたときも継続されるものと考えます。このような場合に自動的にミラーリングしないことも非常に重要です。明示的に選択していないのにデバイス上のほかのコンテンツがストリーミングされてしまうのは、ユーザの望む挙動ではありません。

**アプリでイマーシブ型コンテンツの再生を開始する場合を除き、別のアプリの再生を中断しない。** 例えば、アプリ起動時に再生されるビデオや、アプリで自動再生されるインラインビデオの場合は、そのコンテンツをローカルデバイスでのみ再生し、現在再生中のものが継続できるようにします。デベロッパ向けのガイダンスは、[`ambient`](/documentation/AVFAudio/AVAudioSession/Category-swift.struct/ambient)を参照してください。

**再生中でもアプリのほかの部分を使用できるようにする。** AirPlayがアクティブなときであってもアプリを使えるようにする必要があります。ユーザが再生画面から離れた場合でも、ほかのアプリ内ビデオの再生がストリーミングコンテンツに割り込んで再生されてしまうということがないようにします。

**必要に応じて、メディアの再生を制御するためのカスタムインターフェイスを提供する。** システムで提供されるメディアプレーヤーを使用できない場合は、直観的にAirPlayに切り替えられるカスタムメディアプレーヤーを作成します。その必要がある場合は、再生の開始時、再生中、または再生不可を示す明確な視覚的状態を含め、システムで提供されるものと見た目および動作が一致するカスタムボタンを必ず提供してください。AirPlayを開始するカスタムコントロールではAppleが提供するシンボルのみを使用し、カスタムプレーヤー内の正しい場所（iOS 16以降とiPadOS 16以降では右下隅）にAirPlayアイコンを配置します。

## [AirPlayアイコンの使用](/jp/design/human-interface-guidelines/airplay#Using-AirPlay-icons)

AirPlayアイコンは[リソース](https://developer.apple.com/design/resources/)でダウンロードできます。アプリ内でのAirPlayアイコンの表示には以下のオプションがあります。

### [黒いAirPlayアイコン](/jp/design/human-interface-guidelines/airplay#Black-AirPlay-icon)

背景が白または明るい色で、ほかのテクノロジーアイコンも黒で表示される場合は、黒いAirPlayアイコンを使用します。

![2つの黒いAirPlayアイコン。左はオーディオのAirPlayアイコンです。3つの同心円の下に三角形があります。右はビデオのAirPlayアイコンです。角丸四角形の下に三角形があります。](https://docs-assets.developer.apple.com/published/86e9b97be338e8f54764489242441e37/airplay-black-icon-set%402x.png)

### [白いAirPlayアイコン](/jp/design/human-interface-guidelines/airplay#White-AirPlay-icon)

背景が黒または暗い色で、ほかのテクノロジーアイコンも白で表示される場合は、白いAirPlayアイコンを使用します。

![2つの白いAirPlayアイコン。左はオーディオのAirPlayアイコンです。3つの同心円の下に三角形があります。右はビデオのAirPlayアイコンです。角丸四角形の下に三角形があります。](https://docs-assets.developer.apple.com/published/62baec25a6d8215e9f28971b08bf18b3/airplay-white-icon-set%402x.png)

### [カスタムカラーのAirPlayアイコン](/jp/design/human-interface-guidelines/airplay#Custom-color-AirPlay-icon)

ほかのテクノロジーアイコンがカスタムカラーで表示される場合は、同じカラーを使用します。

![2つの青いAirPlayアイコン。左はオーディオのAirPlayアイコンです。3つの同心円の下に三角形があります。右はビデオのAirPlayアイコンです。角丸四角形の下に三角形があります。](https://docs-assets.developer.apple.com/published/91abb9f30406a70ef7f08541fd4e191b/airplay-custom-color-icon-set%402x.png)

**AirPlayアイコンの配置をほかのテクノロジーアイコンと一致させる。** ほかのテクノロジーアイコンをシェイプの中に表示する場合は、AirPlayアイコンも同様に表示します。

**カスタムボタンまたはインタラクティブな要素ではAirPlayアイコンを使用しない。** AirPlayアイコンおよび _AirPlay_ という名前はインタラクティブでない方法でのみ使用します。

**アイコンと _AirPlay_ の名前を正しく対にする。**ほかのテクノロジーの名前をアイコンの横または下に表示する場合は、AirPlayの名前も同様に表示します。フォントはレイアウト内のほかの部分と同じものを使用してください。AirPlayアイコンをテキスト内で使用したり、 _AirPlay_ という名前の代わりに使用したりしないでください。

**アプリ名をAirPlayより強調する。** AirPlayが自身のアプリの名称やメインアイデンティティよりも目立たないようにします。

## [AirPlayの言及方法](/jp/design/human-interface-guidelines/airplay#Referring-to-AirPlay)

** _AirPlay_ という用語を使うときは適切な大文字化を使用する。** _AirPlay_ は1つの単語からなり、大文字の _A_ と大文字の _P_ の後ろは小文字です。名称がすべて大文字で表示されるレイアウトでは、周囲のスタイルに合わせて _AirPlay_ をすべて大文字で表示してかまいません。

** _AirPlay_ は常に名詞として使用する。**

| テキストの例  
---|---  
![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| AirPlayを使ってスピーカーで聴く  
![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| スピーカーにAirPlayする  
![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| [アプリ名]でAirPlayできる  
  
** _「～で動作する」_ 、 _「使用する」_ 、 _「対応する」_ 、 _「互換性がある」_ などの用語を使用する。**

| テキストの例  
---|---  
![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| [アプリ名]はAirPlayと互換性がある  
![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| AirPlay対応のスピーカー  
![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| [アプリ名]でAirPlayを使用できる  
![丸に囲まれたバツ印が不適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/209f6f0fc8ad99d9bf59e12d82d06584/crossout%402x.png)| [アプリ名]にはAirPlayがある  
  
**必要に応じて _AirPlay_ の名前と共に _Apple_ の名前を使用する。**

| テキストの例  
---|---  
![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| Apple AirPlay対応  
  
**意味を明確にするために適宜AirPlayに言及する。** 特にAirPlayに関連するコンテンツでは、それを明確にするためにAirPlayに言及します。技術仕様でもAirPlayに言及してかまいません。

| テキストの例  
---|---  
![丸に囲まれたチェックマークが適切な使い方であることを示しています。](https://docs-assets.developer.apple.com/published/88662da92338267bb64cd2275c84e484/checkmark%402x.png)| [アプリ名]がAirPlayに対応しました  
  
## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/airplay#Platform-considerations)

 _iOS、iPadOS、macOS、tvOS、visionOSに追加の考慮事項はありません。watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/airplay#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/airplay#Related)

[Appleデザインリソース](https://developer.apple.com/design/resources/)

[Apple商標リスト](https://www.apple.com/legal/intellectual-property/trademark/appletmlist.html)

[Apple商標および著作権使用に関するガイドライン](https://www.apple.com/legal/intellectual-property/guidelinesfor3rdparties.html)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/airplay#Developer-documentation)

[AVFoundation](/documentation/AVFoundation)

[AVKit](/documentation/AVKit)

#### [ビデオ](/jp/design/human-interface-guidelines/airplay#Videos)

[](https://developer.apple.com/videos/play/wwdc2019/501)

## [変更履歴](/jp/design/human-interface-guidelines/airplay#Change-log)

日付| 変更内容  
---|---  
2023年5月02日| ガイダンスを1ページに統合しました。
