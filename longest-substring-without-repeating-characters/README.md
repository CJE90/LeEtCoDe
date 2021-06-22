<h2>3. Longest Substring Without Repeating Characters</h2><h3>Medium</h3><hr><div><p>Given a string <code>s</code>, find the length of the <b>longest substring</b> without repeating characters.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> s = "abcabcbb"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "abc", with the length of 3.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> s = "bbbbb"
<strong>Output:</strong> 1
<strong>Explanation:</strong> The answer is "b", with the length of 1.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> s = "pwwkew"
<strong>Output:</strong> 3
<strong>Explanation:</strong> The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
</pre>

<p><strong>Example 4:</strong></p>

<pre><strong>Input:</strong> s = ""
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= s.length &lt;= 5 * 10<sup>4</sup></code></li>
	<li><code>s</code> consists of English letters, digits, symbols and spaces.</li>
</ul>
</div>

*************************** My Comments ********************************
SLiding window solved with hashset. A difference here is that this solution only needs a for and a while. There never needs to be an if conditions. First we chedk to see if the set contains the character that is at the right position. If not then we add it to the hashset. While the hash does contain what ever is at the right index we need to start removing elements from the left until our window no longer contains the duplication. This cant be done with an if because as long as the duplication exists we need to shrink the window. After each step we need to compute the size of the hashset and this will give us our answer once the for loop is done iterating.

Time Complexity: o(n) as we need to go through the entire array only once.
Space Complexity: potnentially size n for the hashset. We could have a string that is the entire alphabet.
