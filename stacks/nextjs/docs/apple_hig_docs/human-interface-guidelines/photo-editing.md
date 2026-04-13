# 写真編集

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/photo-editing

# 写真編集

写真編集機能拡張では、フィルタなどを適用することによって写真アプリ内の写真やビデオに変更を加えることができます。

![2つの矢印で囲まれている切り取りマークのスケッチ。写真編集を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/95baebfd56c1af886fe0e0cba137cf94/technologies-photo-editing-intro%402x.png)

編集内容は常に新規ファイルとして写真アプリに保存されるため、元のバージョンに影響が及ぶことはありません。

写真編集機能拡張を利用するには、写真を編集モードに切り替える必要があります。編集モードでツールバーの機能拡張アイコンをタップすると、利用可能な編集機能拡張のアクションメニューが表示されます。このうちのいずれかを選択すると、上部のツールバーを含むモーダルビューに機能拡張のインターフェイスが表示されます。ユーザは、このビューを閉じるときに編集内容を確認して保存するか、キャンセルして写真アプリに戻ります。

## [ベストプラクティス](/jp/design/human-interface-guidelines/photo-editing#Best-practices)

**編集内容のキャンセルについてユーザに確認を取る。** 写真やビデオの編集には手間がかかります。キャンセルボタンが押されても編集内容を即座に破棄しないでください。本当にキャンセルしたいかどうかをユーザに尋ね、キャンセルすると編集内容がすべて失われることを知らせましょう。ただし、何も編集が行われていない場合はこの確認メッセージを表示する必要はありません。

**カスタムの上部のツールバーを追加しない。** 機能拡張が読み込まれるモーダルビューにはすでにツールバーがあります。ツールバーが2つもあると紛らわしく、編集対象のコンテンツを表示するスペースも減ってしまいます。

**編集内容のプレビューを表示する。** 編集の結果を確認せずに編集内容を確定するわけにはいきません。機能拡張を閉じて写真アプリに戻る前に、編集結果をユーザが確認できるようにしましょう。

**写真編集機能拡張のアイコンにはアプリアイコンを使用する。** こうすることで、その機能拡張があなたのアプリで提供されたものであることを確実に伝えられます。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/photo-editing#Platform-considerations)

 _iOS、iPadOS、macOSに追加の考慮事項はありません。tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/photo-editing#Resources)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/photo-editing#Developer-documentation)

[App Extension](https://developer.apple.com/app-extensions/)

[PhotoKit](/documentation/PhotoKit)

#### [ビデオ](/jp/design/human-interface-guidelines/photo-editing#Videos)

[](https://developer.apple.com/videos/play/wwdc2019/260)
