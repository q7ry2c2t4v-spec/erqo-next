# Live Photos

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/live-photos

# Live Photos

Live Photosを使用すると、従来の静止画像に音と動きが加わり、お気に入りの思い出がインタラクティブな体験へと生まれ変わります。

![Live Photosアイコンのスケッチ。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/00e2831fd67e472836d94fb1c863e0aa/technologies-Live-Photos-intro%402x.png)

Live Photosを有効にすると、カメラアプリでシャッターを切った前後に追加のコンテンツ（音や追加フレームなど）が取り込まれます。Live Photosの写真を長押しすると、再生されます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/live-photos#Best-practices)

**すべてのフレームに調整を適用する。** アプリでLive Photosに効果や調整を適用する場合は、写真全体に変更を適用します。これに対応しない場合は、静止画像に変換するオプションを提供します。

**Live Photosのコンテンツを保持する。** Live Photosの体験は、すべてのアプリで同じ視覚処理や操作モデルを使用することで、一貫性のあるものにすることが重要です。Live Photosを分解し、フレームや音声を別々に表示しないでください。

**優れた写真共有体験を組み込む。** アプリで写真共有に対応する場合は、共有する前にLive Photosコンテンツ全体をプレビューできるようにします。Live Photosを従来の写真として共有するオプションを必ず提供してください。

**Live Photosがダウンロード中である場合や写真が再生可能な場合は、それを明確に示す。** ダウンロード処理中はプログレスインジケーターを表示します。また、ダウンロードが完了したときに何らかの通知を行います。

**Live Photosに対応していない環境では、Live Photosを従来の写真として表示する。** Live Photosの対応環境と同様の体験を再現しようとしないでください。代わりに、従来の静止画像を表示します。

**Live Photosと静止画像を見分けやすくする。** 写真がLive Photosであることを示す最適な方法は、わずかな動きを表示することです。写真アプリのフルスクリーンブラウザで写真をスワイプするときのようなLive Photosのモーション効果は内蔵されていないため、カスタムのモーション効果をデザインして実装する必要があります。

動きをつけることができない場合は、写真の上にシステムが提供するバッジをテキストあり/なしのいずれかで表示します。視聴者に動画の再生ボタンと間違われるような再生ボタンは含めないでください。

![高山湖の夜間の写真。システムが提供するLive Photosバッジと、左上隅に「Live」というテキストがあります。](https://docs-assets.developer.apple.com/published/a87d82a66bbb1352833d3bf3deb1e325/live-photo-badge-with-text%402x.png)

![高山湖の夜間の写真。システムが提供するLive Photosバッジがあり、左上隅にはテキストはありません。](https://docs-assets.developer.apple.com/published/912dc316a86639661c2f1758145e55db/live-photo-badge%402x.png)

**一貫性のある形でバッジを配置する。** バッジを表示する場合は、すべての写真で同じ位置に配置します。通常は、写真の端にバッジを配置すると見栄えがよくなります。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/live-photos#Platform-considerations)

 _iOS、iPadOS、macOS、tvOSには追加の考慮事項はありません。watchOSには対応していません。_

### [visionOS](/jp/design/human-interface-guidelines/live-photos#visionOS)

visionOSでは、Live Photosの閲覧はできますが、Live Photosを撮ることはできません。

## [リソース](/jp/design/human-interface-guidelines/live-photos#Resources)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/live-photos#Developer-documentation)

[`PHLivePhoto`](/documentation/Photos/PHLivePhoto) — PhotoKit

[LivePhotosKit JS](/documentation/LivePhotosKitJS) — LivePhotosKit JS

#### [ビデオ](/jp/design/human-interface-guidelines/live-photos#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10047)
