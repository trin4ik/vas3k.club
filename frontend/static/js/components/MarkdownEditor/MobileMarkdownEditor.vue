<template>
    <div class="comment-markdown-editor">
        <textarea
            required
            name="text"
            maxlength="20000"
            placeholder="Напишите ответ..."
            ref="textarea"
            :value="value"
            @blur="emitCustomBlur"
        >
        </textarea>
    </div>
</template>

<script>
export default {
    props: {
        value: {
            type: String
        },
        focused: {
            type: Boolean
        }
    },
    mounted: function() {
            this.focusTextareaIfNeeded(this.focused);
    },
    watch: {
        focused: function (value) {
            this.focusTextareaIfNeeded(value);
        }
    },
    methods: {
        emitCustomBlur: function () {
            this.$emit("blur", this.$refs["textarea"].value);
        },
        focusTextareaIfNeeded: function(shouldFocus) {
            this.$nextTick(() => {
                shouldFocus && this.$refs["textarea"].focus();
            });
        }
    }
}
</script>
