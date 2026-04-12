# 近距離インタラクション

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/nearby-interactions

# 近距離インタラクション

近距離インタラクションにより、近距離の環境内に人とオブジェクトの両方を存在させる体験をデバイス上で実現できます。

![小さな円を含む円形の領域の横に、曲線が描かれたスケッチ。部屋の中で特定の方向から人に近づく音声を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる紫色になっています](https://docs-assets.developer.apple.com/published/4ee9418314d3a8bbdc8e7586a9e3c787/inputs-nearby-interactions-intro%402x.png)

近距離インタラクションは、人が生まれながらに持つ空間認識を利用するので、直感的で自然に感じられるものにすると優れた体験になります。例えば、iPhoneでミュージックを再生しているユーザは、デバイスをHomePod miniに近づけることで、iPhoneからのオーディオ出力を転送して、そのままHomePod miniで聴くことができます。

近距離インタラクションは、超広帯域無線テクノロジーに対応しているデバイスで利用でき（詳しくは[超広帯域無線の対応状況](https://support.apple.com/en-us/HT212274)を参照）、[Nearby Interaction](/documentation/NearbyInteraction)フレームワークを使用します。近距離インタラクションの体験に入るには、アプリの使用中にユーザがデバイスにインタラクションの許可を与える必要があります。Nearby InteractionのAPIでは、ランダムに生成されたデバイス識別子を、アプリが開始したインタラクションセッションの間だけ使用するので、ユーザのプライバシーが保護されます。

## [ベストプラクティス](/jp/design/human-interface-guidelines/nearby-interactions#Best-practices)

**タスクを物理世界の観点で見て近距離インタラクションの着想を得る。** 例えば、アプリのUIを使用して曲をiPhoneからHomePod miniに転送するのは簡単ですが、デバイスを近づけるだけで転送を開始できれば、物理世界の体験により深く根ざしたタスクであると感じられます。タスクの概念を特徴付けるような物理的アクションを見出すことで、簡単で自然に実行できる魅力的な体験を生み出せます。

**距離、方向、状況についての情報をインタラクションに取り入れる。** アプリにはさまざまな情報源があるかもしれませんが、状況に適した近くの情報を優先することで、有機的に感じられる体験を提供できます。例えば、混雑した部屋で友人とコンテンツを共有したい場合なら、ユーザがよく連絡する人や最近連絡した人についてのデバイス上の情報を活用して、iOSの共有シートで受信者を提案できます。この知識と、U1チップが搭載された近くにあるデバイスの情報を組み合わせ、最も適切な連絡先を共有シートで提案することで、より優れた体験を提供することができます。

**物理的な距離の変化によって近距離インタラクションにどのような影響を与えられるかを検討する。** 通常、物理世界では、物体が近くにあるほど認識力が高まります。物体との距離に応じてフィードバックを変化させると、近距離インタラクションでこれを模倣できます。例えば、iPhoneでAirTagを探すときは、ユーザがAirTagに近づくと、表示が方向を示す矢印から脈動する円に変わります。

**フィードバックを継続的に提供する。** フィードバックが途切れないようにすると、物理世界の変化が反映され、近距離インタラクションと実行中のタスクとの結びつきが強くなります。例えば、「探す」で紛失物を探す場合、継続的に方向と近さに関する最新情報を得ることができます。移動に反応して中断のないフィードバックを提供することで、タスクに対するユーザの関心が途切れないようにします。

**総合的な体験を生み出すために、複数種類のフィードバックを使用することを検討する。** 視覚、聴覚、触覚へのフィードバックを滑らかに切り替えると、近距離インタラクションのタスクとの関係性が強まり、よりリアルに感じられます。また、複数の種類のフィードバックを使用することで、タスクと現在の状況の両方に対応できるように体験を変化させることができます。例えば、ユーザがデバイスの画面に注意を向けているときは視覚フィードバックが適しています。ユーザが周囲の環境に注意を向けているときは、聴覚や触覚でのフィードバックが適しています。

**近距離インタラクションをタスクを実行する唯一の方法にしない。** すべてのユーザが近距離インタラクションを利用できるとは限らないので、アプリ内のタスクを別の手段でも実行できるようにしておくことが不可欠です。

## [デバイスの使用](/jp/design/human-interface-guidelines/nearby-interactions#Device-usage)

**デバイスを縦向きに持つことを推奨する。** デバイスを横向きに持つと、ほかのデバイスとの距離や相対的な方向に関する情報の精度と可用性が下がることがあります。縦向きでしか近距離インタラクションの機能を実行できない場合は、最適な体験につながるデバイスの持ち方を視覚的にそれとなく伝えるとよいでしょう。デバイスを縦向きにするように明示的に伝えることは、できる限り避けてください。

**デバイスの方向的視野を考慮してデザインする。** 近くのデバイスとのインタラクションには、iPhone 11以降の超広角カメラと同等の視野を持つハードウェアセンサーを使用します。インタラクションに参加するデバイスがこの視野から外れている場合、アプリで相対的な方向を受信できず、距離だけを受信する場合があります。

**近くのデバイスとのインタラクションには障害物が影響する可能性があることを伝える。** インタラクションに参加している2台のデバイスの間に、人や動物などのような大きな物体が入り込むと、距離情報や方向情報の精度や可用性が低下する可能性があります。オンボーディングやチュートリアルのコンテンツを提示する際に、こうした状況を避けるよう助言することを検討してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/nearby-interactions#Platform-considerations)

 _iPadOSに追加の考慮事項はありません。macOS、tvOS、visionOSには対応していません。_

### [iOS](/jp/design/human-interface-guidelines/nearby-interactions#iOS)

iPhoneでは、Nearby InteractionのAPIによって、ペアとなるデバイスの距離と方向が提供されます。

### [watchOS](/jp/design/human-interface-guidelines/nearby-interactions#watchOS)

Apple Watchでは、Nearby InteractionのAPIによって、ペアとなるデバイスの距離が提供されます。また、近くのデバイスとのインタラクションに参加するすべてのwatchOSアプリは、フォアグラウンドで動作している必要があります。

## [リソース](/jp/design/human-interface-guidelines/nearby-interactions#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/nearby-interactions#Related)

[フィードバック](/jp/design/human-interface-guidelines/feedback)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/nearby-interactions#Developer-documentation)

[Nearby Interaction](/documentation/NearbyInteraction)

#### [ビデオ](/jp/design/human-interface-guidelines/nearby-interactions#Videos)

[](https://developer.apple.com/videos/play/wwdc2021/10245)

[](https://developer.apple.com/videos/play/wwdc2020/10668)

## [変更履歴](/jp/design/human-interface-guidelines/nearby-interactions#Change-log)

日付| 変更内容  
---|---  
2023年6月21日| ページタイトルを「空間インタラクション」から変更。
